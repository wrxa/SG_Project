package util;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.Set;
import java.util.TreeSet;

/**
 * 
 * @author ren.bo2
 *
 */
public class MainOrder {
	public static void main(String[] args) throws IOException {
		//		creatContantJson("constant.properties");
		//		creatccpp_ccppContantJson("ccpp_ccpp_aonatant.properties");
		//		creatModelMain();
		//		planTriggerMain();
		creatTableInTriggerAndTriggerFunctionMain();
//		creatTableBetweenTriggerAndTriggerFunctionMain();
	}

	/**
	 * 生成模型主方法
	 * @throws FileNotFoundException
	 */
	public static void creatModelMain() throws FileNotFoundException {
		//		String tablename = "ccpp_needsQuestionnaire";
		//		String inputFileName = "ccpp需求调查表输入原始文件.properties";

		String tablename = "ccpp_ccpp";
		String inputFileName = "ccpp计算原始数据文件.properties";
		String flagxh = "check";
		String flagsj = "design";
		String flagbz = "remarks";
		PrintStream oldps = System.out;
		OutputStream os = new FileOutputStream(tablename + ".model");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		creatModel(inputFileName, tablename, flagxh, flagsj, null);
		System.setOut(oldps);
	}

	/**
	 * 方案表的触发动作
	 * @param tableNames
	 * @throws FileNotFoundException
	 */
	public static void planTriggerMain() throws FileNotFoundException {
		String[] tableNames = { "ccpp_ccpp", "ccpp_needs_questionnaire" };
		PrintStream oldps = new PrintStream(System.out);
		OutputStream os = new FileOutputStream("plan触发动作.sql");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		planTrigger(tableNames);
		System.setOut(oldps);
	}

	/**
	 * 创建表内触发动作主方法
	 * @throws IOException
	 */
	public static void creatTableInTriggerAndTriggerFunctionMain() throws IOException {
		String tablename = "gaspowergeneration_boiler_of_pts";
		String flagxh = "check";
		//String flagsj = "design";
		String excleColumn = "F";
		ConversionFormula(excleColumn);//生成cache文件
		Properties prop = readOrderedPropertiesFile("cache.properties");
		Map<String, String> map = creatGZiduanMap(prop, excleColumn);
		Map<String, String> mapNotes = getNotesMap(prop);
		PrintStream oldps = System.out;
		OutputStream os = new FileOutputStream("In_the_table_boiler_Trigger.sql");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		tableInTriggerFunction(prop, map, mapNotes, tablename, flagxh, excleColumn);
		tableInTrigger(prop, map, mapNotes, tablename, flagxh, excleColumn);
		System.out.println();
		//tableInTriggerFunction(prop, map, mapNotes, tablename, flagsj, excleColumn);
		//tableInTrigger(prop, map, mapNotes, tablename, flagsj, excleColumn);
		//System.setOut(oldps);
	}

	/**
	 * 创建表间触发动作的主方法(同步数据)
	 * tableaname表数据同步到->tablenbame
	 * @throws IOException
	 */
	public static void creatTableBetweenTriggerAndTriggerFunctionMain() throws IOException {
		Properties prop = readOrderedPropertiesFile("between_the_table_inputTrigger.properties");
		String atablename = "gaspowergeneration_needsquestionnaire";
		String btablenname = "gaspowergeneration_boiler_of_pts";
		PrintStream oldps = System.out;
		OutputStream os = new FileOutputStream("between_needsquestionnaire_and_boiler.sql");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		printProp(prop, atablename, btablenname);
		System.setOut(oldps);
	}

	/********************************************************表内触发器和触发函数的创建**********************************************************************************/

	public static void ConversionFormula(String flg) throws IOException {
		OutputStream os = new FileOutputStream("cache.properties");
		PrintStream oldps = System.out;
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		Properties props = new OrderedProperties();
		FileInputStream fileInputStream = new FileInputStream("In_the_table_inputTrigger.properties");
		props.load(fileInputStream);
		// 用于存储所有节点  
		Map<String, String> map = new HashMap<String, String>();
		for (Object key : props.keySet()) {
			if (props.getProperty(key.toString()).split("=").length > 1) {
				map.put(flg + key.toString().split("#")[0], flg + key.toString().split("#")[0] + "=" + props.getProperty(key.toString()).split("=")[1]);
			} else {
				map.put(flg + key.toString().split("#")[0], flg + key.toString().split("#")[0] + "=");
			}
		}
		/**
		 * 递归实现搜索替换
		 */
		for (Object key : props.keySet()) {
			if (props.getProperty(key.toString()).split("=").length > 1) {
				String newstr = th(map, props.getProperty(key.toString()).split("=")[1], flg);
				System.out.println(key + ":" + props.getProperty(key.toString()).split("=")[0] + "=" + newstr);
			} else {
				System.out.println(key + ":" + props.getProperty(key.toString()).split("=")[0] + "=");
			}
		}
		System.setOut(oldps);
	}

	public static String th(Map<String, String> map, String dd, String flg) {
		String[] arrayStr = dd.split("\\+|\\(|\\)|\\*|/|\\-");
		// 去除数组中为空的字符串  
		List<String> tmp = new ArrayList<String>();
		for (String str : arrayStr) {
			if (str != null && str.startsWith(flg)) {
				tmp.add(str);
			}
		}
		arrayStr = tmp.toArray(new String[0]);
		for (String str : arrayStr) {
			String newstr = str;
			if (map.get(newstr).split("=").length > 1) {
				dd = dd.replaceAll(newstr, "(" + map.get(newstr).split("=")[1] + ")");
				dd = th(map, dd, flg);
			}
		}
		return dd;
	}

	public static Map<String, String> creatGZiduanMap(Properties properties, String excleColumn) {
		Map<String, String> map = new HashMap<String, String>();
		for (String key : properties.stringPropertyNames()) {
			map.put(excleColumn + key.split("#")[0], properties.getProperty(key).split("=")[0]);
		}
		return map;
	}

	public static Map<String, String> getNotesMap(Properties properties) {
		Map<String, String> map = new HashMap<String, String>();
		for (String key : properties.stringPropertyNames()) {
			map.put(properties.getProperty(key).split("=")[0], key.split("#")[1]);
		}
		return map;
	}

	/**
	 * 创建触发函数
	 * @param properties
	 * @return
	 * @throws FileNotFoundException 
	 */
	public static void tableInTriggerFunction(Properties properties, Map<String, String> map, Map<String, String> mapNotes, String tablename, String flag, String excleColumn)
			throws FileNotFoundException {
		int i = 1;
		/**
		 * 创建触发函数头
		 */
		//System.out.println("CREATE OR REPLACE FUNCTION " + tablename + "_" + flag + "()");
		System.out.println("CREATE OR REPLACE FUNCTION " + tablename  + "()");
		System.out.println("RETURNS TRIGGER AS");
		System.out.println("$BODY$");
		System.out.println("BEGIN");
		/**
		 * 创建触发函数体
		 */
		for (String key : properties.stringPropertyNames()) {
			if (properties.getProperty(key).split("=").length > 1) {
				gzdih(properties.getProperty(key).split("=")[1], map, mapNotes, properties.getProperty(key).split("=")[0], i, flag, tablename, excleColumn);
				i += 1;
			}

		}
		/**
		 * 创建触发函数尾
		 */
		System.out.println("RETURN NULL;");
		System.out.println("END;");
		System.out.println("$BODY$");
		System.out.println("LANGUAGE 'plpgsql' VOLATILE;");
		System.out.println();
	}

	/**
	 * 创建触发函数体
	 * @param str
	 * @param map
	 * @param strright
	 */
	public static void gzdih(String str, Map<String, String> map, Map<String, String> mapNotes, String strright, int i, String fg, String tablename, String excleColumn) {
		String[] arrSt = str.split("\\*|/|\\(|\\)|\\+|\\-");
		//将arrSt排序：由大到小

		System.out.println("----------------------实现字段" + strright + ":" + mapNotes.get(strright) + ",的计算" + i + "-----------------------------------");
		String dddString = "  IF ";
		String str_sj = str;
		Set set_sj = new TreeSet();
		for (String str1 : arrSt) {
			if (str1.startsWith(excleColumn)) {
				set_sj.add(str1);
			}
		}
		String[] arrSt_sj = (String[]) set_sj.toArray(new String[0]);
		for (String str1 : arrSt_sj) {
			//String sead = map.get(str1) + "_" + fg + "";
			String sead = map.get(str1) + "";
			if (str1.equals(arrSt_sj[arrSt_sj.length - 1])) {
				dddString += "OLD." + sead + " != NEW." + sead + "";
			} else {
				dddString += "OLD." + sead + " != NEW." + sead + " OR ";
			}
		}

		dddString += " THEN";
		System.out.println(dddString);
		System.out.println("     update " + tablename + " set ");
		System.out.println();
		//生成公式
		sort(arrSt_sj, excleColumn);
		for (String str1 : arrSt_sj) {
			//str_sj = str_sj.replaceAll(str1, "NEW." + map.get(str1) + "_" + fg + "");
			str_sj = str_sj.replaceAll(str1, "NEW." + map.get(str1) + "");
		}
		//System.out.println("     " + strright + "_" + fg + "=" + str_sj + "");
		System.out.println("     " + strright + "=" + str_sj + "");
		System.out.println("     where plan_id=NEW.plan_id;");
		System.out.println();

		dddString = "  ELSIF (";
		for (String str1 : arrSt_sj) {
			//String sead = map.get(str1) + "_" + fg + "";
			String sead = map.get(str1) + "";
			if (str1.equals(arrSt_sj[arrSt_sj.length - 1])) {
				dddString += "OLD." + sead + " ISNULL) AND ";
			} else {
				dddString += "OLD." + sead + " ISNULL OR ";
			}
		}
		for (String str1 : arrSt_sj) {
			//String sead = map.get(str1) + "_" + fg + "";
			String sead = map.get(str1) + "";
			if (str1.equals(arrSt_sj[arrSt_sj.length - 1])) {
				dddString += "NEW." + sead + " NOTNULL";
			} else {
				dddString += "NEW." + sead + " NOTNULL AND ";
			}
		}

		dddString += " THEN";
		System.out.println(dddString);
		System.out.println("     update " + tablename + " set ");
		System.out.println();
		//生成公式
		for (String str1 : arrSt_sj) {
			//str_sj = str_sj.replaceAll(str1, "NEW." + map.get(str1) + "_" + fg + "");
			str_sj = str_sj.replaceAll(str1, "NEW." + map.get(str1) + "");
		}
		//System.out.println("     " + strright + "_" + fg + "=" + str_sj + "");
		System.out.println("     " + strright + "=" + str_sj + "");
		System.out.println("     where plan_id=NEW.plan_id;");
		System.out.println();

		System.out.println("  END IF;");
	}

	/**
	 * 由大到小排序
	 * @param num
	 */
	public static void sort(String[] num, String flg) {
		int j = 0;
		while (j < num.length) {
			for (int i = 0; i < num.length - 1; i++) {
				if (Integer.parseInt(num[i].split(flg)[1]) < Integer.parseInt(num[i + 1].split(flg)[1])) {
					String temp;
					temp = num[i];
					num[i] = num[i + 1];
					num[i + 1] = temp;
				}
			}
			j++;
		}
	}

	/**
	 * 创建触发器
	 * @param properties
	 * @param map
	 * @throws FileNotFoundException 
	 */
	public static void tableInTrigger(Properties properties, Map<String, String> map, Map<String, String> mapNotes, String tablename, String flag, String excleColumn) throws FileNotFoundException {
		/**
		 * 触发器头
		 */
		System.out.println();
		System.out.println("--创建触发器");
		//		System.out.println("DELETE FROM pg_trigger WHERE tgname='" + tablename + "_" + flag + "';");
		//System.out.println("CREATE TRIGGER \"" + tablename + "_" + flag + "\" AFTER UPDATE OF");
		System.out.println("CREATE TRIGGER \"" + tablename + "\" AFTER UPDATE OF");
		
		String dddString = "";
		Set set = new TreeSet();
		for (String key : properties.stringPropertyNames()) {
			if (properties.getProperty(key).split("=").length > 1) {
				setTriggerField(properties.getProperty(key).split("=")[1], set, excleColumn);
			}
		}
		String[] arrSt_sj = (String[]) set.toArray(new String[0]);
		/**
		 * 构造触发器体
		 */
		for (String str1 : arrSt_sj) {
			//String sead = map.get(str1) + "_" + flag + "";
			String sead = map.get(str1) + "";
			if (str1.equals(arrSt_sj[arrSt_sj.length - 1])) {
				System.out.println("\"" + sead + "\"");
			} else {
				System.out.println("\"" + sead + "\",");
			}
		}
		/**
		 * 触发器尾
		 */
		System.out.println("ON \"public\".\"" + tablename + "\"");
		System.out.println("FOR EACH ROW");
		//System.out.println("EXECUTE PROCEDURE \"" + tablename + "_" + flag + "\"();");
		System.out.println("EXECUTE PROCEDURE \"" + tablename + "\"();");
	}

	/**
	 * 获得触发器触发字段集
	 * @param str
	 * @param map
	 * @param strright
	 */
	public static void setTriggerField(String str, Set set, String excleColumn) {
		String[] arrSt = str.split("\\*|/|\\(|\\)|\\+|\\-");
		String str_sj = str;
		for (String str1 : arrSt) {
			if (str1.startsWith(excleColumn)) {
				set.add(str1);
			}
		}
	}

	/*********************************************************表间触发器和触发函数的创建*************************************************************************************/
	/**
	 * 输出properties的key和value
	 * atablename的字段同步到表btablename
	 * @throws FileNotFoundException 
	 */
	public static void printProp(Properties properties, String atablename, String btablename) throws FileNotFoundException {
		System.out.println("----------------------创建触发函数-----------------------------------");
		creatTriggerFunction(properties, atablename, btablename);
		System.out.println("----------------------创建触发器-----------------------------------");
		creatTrigger(properties, atablename, btablename);
	}

	/**
	 * 创建需求表和锅炉计算表触发器函数
	 * @param properties
	 */
	public static void creatTriggerFunction(Properties properties, String atablename, String btablename) {
		for (String key : properties.stringPropertyNames()) {
			System.out.println("--用于同步表："
				+ atablename
				+ "的"
				+ key
				+ "字段，和表"
				+ btablename
				+ "的"
				+ properties.getProperty(key)
				+ "字段，即："
				+ btablename
				+ "."
				+ key
				+ "="
				+ atablename
				+ "."
				+ properties.getProperty(key));
			System.out.println("CREATE OR REPLACE FUNCTION " + btablename + "_" + key + "()");
			System.out.println("RETURNS TRIGGER AS");
			System.out.println("$BODY$");
			System.out.println("BEGIN");
			System.out.println("  update " + btablename + " set " + key + "=" + atablename + "." + properties.getProperty(key) + "");
			System.out.println("  from " + atablename + " where " + atablename + ".plan_id=" + btablename + ".plan_id;");
			System.out.println("RETURN NULL;");
			System.out.println("END;");
			System.out.println("$BODY$");
			System.out.println("LANGUAGE 'plpgsql' VOLATILE;");
			System.out.println();
			System.out.println();
		}
	}

	/**
	 * 创建需求表触发器
	 * @param properties
	 */
	public static void creatTrigger(Properties properties, String atablename, String btablename) {
		int i = 0;
		System.out.println();
		for (String key : properties.stringPropertyNames()) {
			System.out.println("--该触发器用于：当" + properties.getProperty(key) + "有更新时触发" + btablename + "." + key + "=" + atablename + "." + properties.getProperty(key) + "");
			//			System.out.println("DELETE FROM pg_trigger WHERE tgname='" + atablename + "_a_" + i + "';");
			System.out.println("CREATE TRIGGER \"" + atablename + "_a_" + i + "\" AFTER UPDATE OF \"" + properties.getProperty(key) + "\" ON \"public\".\"" + atablename + "\"");
			System.out.println("FOR EACH ROW");
			System.out.println("EXECUTE PROCEDURE \"" + btablename + "_" + key + "\"();");
			System.out.println();
			System.out.println();
			i++;
		}
	}

	/*******************************************************************生成模型**************************************************************************/
	public static void creatModel(String inputFileName, String tablename, String flagxh, String flagsj, String flagbz) throws FileNotFoundException {
		System.out.println("# -*- coding: utf-8 -*-");
		System.out.println("from app import db");
		System.out.println();
		System.out.println();
		System.out.println("class " + upperCase(tablename) + "(db.Model):");
		System.out.println("    # 表名");
		System.out.println("    __tablename__ = '" + tablename + "'");
		System.out.println("    # 表ID,自动生成（主键）");
		System.out.println("    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)");
		System.out.println("    # 方案ID(外键)");
		System.out.println("    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))");
		Properties properties = readOrderedPropertiesFile(inputFileName);
		for (String key : properties.stringPropertyNames()) {
			if (key.split("#").length > 1) {
				if (flagsj != null) {
					System.out.println("    # " + key.split("#")[1] + "设计值");
					System.out.println("    " + properties.getProperty(key).split("=")[0] + "_" + flagsj + " = db.Column(db.NUMERIC(precision=15, scale=5))");
					//					System.out.println("    # " + key.split("#")[1]);
					//					System.out.println("    " + properties.getProperty(key).split("=")[0] + " = db.Column(db.NUMERIC(precision=15, scale=5))");
				}

				if (flagxh != null) {
					System.out.println("    # " + key.split("#")[1] + ":校核值");
					System.out.println("    " + properties.getProperty(key).split("=")[0] + "_" + flagxh + " = db.Column(db.NUMERIC(precision=15, scale=5))");
				}

				//				if (flagbz != null) {
				//					System.out.println("    # " + key.split("#")[1] + ":备注值");
				//					System.out.println("    " + properties.getProperty(key).split("=")[0] + "_" + flagbz + " = db.Text())");
				//				}
			} else {
				if (flagsj != null) {
					//					System.out.println("    # " + key.split("#")[1] + "设计值");
					//					System.out.println("    " + properties.getProperty(key).split("=")[0] + "_" + flagsj + " = db.Column(db.NUMERIC(precision=15, scale=5))");
					System.out.println("    # " + key + ":设计值");
					System.out.println("    " + properties.getProperty(key) + "_" + flagsj + " = db.Column(db.NUMERIC(precision=15, scale=5))");
				}

				if (flagxh != null) {
					System.out.println("    # " + key + ":校核值");
					System.out.println("    " + properties.getProperty(key) + "_" + flagxh + " = db.Column(db.NUMERIC(precision=15, scale=5))");
				}
				//				if (flagbz != null) {
				//					System.out.println("    # " + key + ":备注值");
				//					System.out.println("    " + properties.getProperty(key) + "_" + flagbz + " = db.Column(db.Text(), nullable=True)");
				//				}
			}
			System.out.println();
		}
	}

	/********************************************************************方案表的触发器********************************************************************************/
	public static void planTrigger(String[] tableNames) throws FileNotFoundException {
		System.out.println("CREATE OR REPLACE FUNCTION plan_id_insert()");
		System.out.println("RETURNS TRIGGER AS");
		System.out.println("$BODY$");
		System.out.println("DECLARE");
		System.out.println("  NEWIDD integer;");
		System.out.println();
		System.out.println("BEGIN");
		System.out.println("    NEWIDD = NEW.id;");
		System.out.println("		IF TG_OP='INSERT' THEN");
		for (String str : tableNames) {
			System.out.println("		   INSERT INTO " + str + " (plan_id) VALUES (NEWIDD);");
		}
		System.out.println("       RETURN NULL;");
		System.out.println("	  END IF;");
		System.out.println("END;");
		System.out.println("$BODY$");
		System.out.println("LANGUAGE 'plpgsql' VOLATILE;");
		System.out.println();
		//		System.out.println("DELETE FROM pg_trigger WHERE tgname='plan_a_000001';");
		System.out.println("--删除级联记录");
		System.out.println("CREATE TRIGGER plan_a_000001");
		System.out.println("AFTER INSERT ON plan");
		System.out.println("FOR EACH ROW EXECUTE PROCEDURE plan_id_insert();");
	}

	/*********************************************************生成常量******************************************************************/
	public static void creatContantJson(String inputFileName) throws FileNotFoundException {
		PrintStream oldps = new PrintStream(System.out);
		OutputStream os = new FileOutputStream("questionnaire.contant");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		Properties properties = readOrderedPropertiesFile(inputFileName);
		System.out.println("# ccpp需求调查表");
		System.out.println("ccpp_questionnaire_data = [{");
		for (String key : properties.stringPropertyNames()) {
			System.out.println("    \"module_name\": \"ccpp_questionnaire\",");
			System.out.println("    \"name_eng\": \"" + properties.getProperty(key).split("###")[0] + "\",");
			System.out.println("    \"name\": u\"" + key + "\",");
			System.out.println("    \"symbol\": u\"" + properties.getProperty(key).split("###")[1] + "\",");
			System.out.println("    \"unit\": u\"" + properties.getProperty(key).split("###")[2] + "\",");
			System.out.println("    \"calculate\": u\"" + properties.getProperty(key).split("###")[3] + "\",");
			System.out.println("    \"remark\": u\"" + properties.getProperty(key).split("###")[4] + "\",");
			System.out.println("    \"defaultvalue\": u\"" + properties.getProperty(key).split("###")[5] + "\",");
			System.out.println("    \"minmodelid\": u\"" + properties.getProperty(key).split("###")[6] + "\",");
			System.out.println("    \"controltype\": u\"" + properties.getProperty(key).split("###")[7] + "\",");
			System.out.println("    \"jurisdiction\": u\"" + properties.getProperty(key).split("###")[8] + "\"");
			System.out.println("}, {");
		}
		System.setOut(oldps);

	}

	public static void creatccpp_ccppContantJson(String inputFileName) throws FileNotFoundException {
		PrintStream oldps = new PrintStream(System.out);
		OutputStream os = new FileOutputStream("ccpp.contant");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		Properties properties = readOrderedPropertiesFile(inputFileName);
		System.out.println("# -*- coding: utf-8 -*-");
		System.out.println("from constant import CcppConstant");
		System.out.println();
		System.out.println();
		System.out.println("# ccpp计算表");
		System.out.println("ccpp_ccpp_data = [{");
		for (String key : properties.stringPropertyNames()) {
			System.out.println("    \"module_name\": \"ccpp_ccpp\",");
			System.out.println("    \"name_eng\": \"" + key + "\",");

			if (properties.getProperty(key).split("###").length > 3) {
				System.out.println("    \"name\": u\"" + properties.getProperty(key).split("###")[4] + "\",");
			} else {
				System.out.println("    \"name\": u\"\",");
			}

			if (properties.getProperty(key).split("###").length > 4) {
				System.out.println("    \"symbol\": u\"" + properties.getProperty(key).split("###")[5] + "\",");
			} else {
				System.out.println("    \"symbol\": u\"\",");
			}
			if (properties.getProperty(key).split("###").length > 5) {
				System.out.println("    \"unit\": u\"" + properties.getProperty(key).split("###")[6] + "\",");
			} else {
				System.out.println("    \"unit\": u\"\",");
			}

			if (properties.getProperty(key).split("###").length > 6) {
				System.out.println("    \"calculate\": u\"" + properties.getProperty(key).split("###")[7] + "\",");
			} else {
				System.out.println("    \"calculate\": u\"\",");
			}
			if (properties.getProperty(key).split("###").length > 7) {
				System.out.println("    \"remark\": u\"" + properties.getProperty(key).split("###")[8] + "\",");
			} else {
				System.out.println("    \"remark\": u\"\",");
			}
			if (properties.getProperty(key).split("###").length > 8) {
				System.out.println("    \"defaultvalue\": u\"" + properties.getProperty(key).split("###")[9] + "\",");
			} else {
				System.out.println("    \"defaultvalue\": u\"\",");
			}
			if (properties.getProperty(key).split("###").length > 9) {
				System.out.println("    \"minmodelid\": u\"" + properties.getProperty(key).split("###")[10] + "\",");
			} else {
				System.out.println("    \"minmodelid\": u\"\",");
			}
			if (properties.getProperty(key).split("###").length > 10) {
				System.out.println("    \"controltype\": u\"" + properties.getProperty(key).split("###")[11] + "\",");
			} else {
				System.out.println("    \"controltype\": u\"\",");
			}
			if (properties.getProperty(key).split("###").length > 11) {
				System.out.println("    \"jurisdiction\": u\"" + properties.getProperty(key).split("###")[12] + "\"");
			} else {
				System.out.println("    \"jurisdiction\": u\"\"");
			}
			System.out.println("}, {");
		}
		System.setOut(oldps);
	}

	/****************************************************************************************************************************************************/
	/**
	 * 读Properties文件（有序）
	 */
	private static Properties readOrderedPropertiesFile(String filename) {
		Properties properties = new OrderedProperties();
		InputStreamReader inputStreamReader = null;
		try {
			InputStream inputStream = new BufferedInputStream(new FileInputStream(filename));
			//prop.load(in);//直接这么写，如果properties文件中有汉子，则汉字会乱码。因为未设置编码格式。
			inputStreamReader = new InputStreamReader(inputStream, "utf-8");
			properties.load(inputStreamReader);
		} catch (Exception e) {
			//			System.out.println(e.getMessage());
		} finally {
			if (inputStreamReader != null) {
				try {
					inputStreamReader.close();
				} catch (IOException e) {
					//					System.out.println(e.getMessage());
				}
			}
		}
		return properties;
	}

	public static String upperCase(String str) {
		char[] ch = str.toCharArray();
		if (ch[0] >= 'a' && ch[0] <= 'z') {
			ch[0] = (char) (ch[0] - 32);
		}
		return new String(ch);
	}
}
//System.out.println("---------（方式二）------------");
//		Set<Object> keys = properties.keySet();//返回属性key的集合
//		for (Object key : keys) {
//			System.out.println(key.toString() + "=" + properties.get(key));
//		}
//
//		System.out.println("---------（方式三）------------");
//		Set<Map.Entry<Object, Object>> entrySet = properties.entrySet();//返回的属性键值对实体
//		for (Map.Entry<Object, Object> entry : entrySet) {
//			System.out.println(entry.getKey() + "=" + entry.getValue());
//		}
//
//		System.out.println("---------（方式四）------------");
//		Enumeration<?> e = properties.propertyNames();
//		while (e.hasMoreElements()) {
//			String key = (String) e.nextElement();
//			String value = properties.getProperty(key);
//			System.out.println(key + "=" + value);
//		}

