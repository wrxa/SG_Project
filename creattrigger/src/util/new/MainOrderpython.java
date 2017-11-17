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
public class MainOrderpython {
	public static void main(String[] args) throws IOException {
		creatTableInTriggerAndTriggerFunctionMain();
	}

	/**
	 * 创建表内触发动作主方法
	 * @throws IOException
	 */
	public static void creatTableInTriggerAndTriggerFunctionMain() throws IOException {
		String tablename = "ccpp_ccpp";
		String flagxh = "";
		String flagsj = "_design";
		String excleColumn = "G";
		FileInputStream fileInputStream = new FileInputStream("123456.properties");
		ConversionFormula(fileInputStream, excleColumn);
		Map<String, String> map = creatGZiduanMap();
		Map<String, String> mapNotes = getNotesMap();
		PrintStream oldps = System.out;
		OutputStream os = new FileOutputStream("输出文件.sql");
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		System.out.println();
		tableInTriggerPython(map, mapNotes, tablename, flagsj);
		System.setOut(oldps);
	}

	/********************************************************搜索替换**********************************************************************************/

	public static void ConversionFormula(FileInputStream fileInputStream, String excleColumn) throws IOException {
		OutputStream os = new FileOutputStream("cache.properties");
		PrintStream oldps = System.out;
		PrintStream newps = new PrintStream(os);
		System.setOut(newps);
		Properties props = new OrderedProperties();
		props.load(fileInputStream);
		// 用于存储所有节点  
		Map<String, String> map = new HashMap<String, String>();
		for (Object key : props.keySet()) {
			if (props.getProperty(key.toString()).split("=").length > 1) {
				map.put(excleColumn + key.toString().split("#")[0], excleColumn + key.toString().split("#")[0] + "=" + props.getProperty(key.toString()).split("=")[1]);
			} else {
				map.put(excleColumn + key.toString().split("#")[0], excleColumn + key.toString().split("#")[0] + "=");
			}
		}

		/**
		 * 递归实现搜索替换
		 */
		for (Object key : props.keySet()) {
			if (props.getProperty(key.toString()).split("=").length > 1) {
				String newstr = th(map, props.getProperty(key.toString()).split("=")[1], excleColumn);
				System.out.println(key + ":" + props.getProperty(key.toString()).split("=")[0] + "=" + newstr);
			} else {
				System.out.println(key + ":" + props.getProperty(key.toString()).split("=")[0] + "=");
			}
		}
		System.setOut(oldps);
	}

	public static String th(Map<String, String> map, String dd, String excleColumn) {
		String[] arrayStr = dd.split("\\+|\\(|\\)|\\*|/|\\-|,");
		// 去除数组中为空的字符串  
		List<String> tmp = new ArrayList<String>();
		for (String str : arrayStr) {
			if (str != null && str.startsWith(excleColumn)) {
				tmp.add(str);
			}
		}
		arrayStr = tmp.toArray(new String[0]);
		sort(arrayStr, excleColumn);
		for (String str : arrayStr) {
			String newstr = str;
			if (map.get(newstr).split("=").length > 1) {
				dd = dd.replaceAll(newstr, "(" + map.get(newstr).split("=")[1] + ")");
				dd = th(map, dd, excleColumn);
			} else {
				//深度搜索到叶子节点，替换
				dd = dd.replaceAll(newstr, "(" + map.get(newstr).split("=")[0].replaceAll(excleColumn, "MM") + ")");
			}
		}
		return dd;
	}

	public static Map<String, String> creatGZiduanMap() {
		Properties properties = readOrderedPropertiesFile("cache.properties");
		Map<String, String> map = new HashMap<String, String>();
		for (String key : properties.stringPropertyNames()) {
			map.put("MM" + key.split("#")[0], properties.getProperty(key).split("=")[0]);
		}
		return map;
	}

	public static Map<String, String> getNotesMap() {
		Properties properties = readOrderedPropertiesFile("cache.properties");
		Map<String, String> map = new HashMap<String, String>();
		for (String key : properties.stringPropertyNames()) {
			map.put(properties.getProperty(key).split("=")[0], key.split("#")[1]);
		}
		return map;
	}

	/**
	 * 创建python类
	 * @param properties
	 * @return
	 * @throws FileNotFoundException 
	 */
	public static void tableInTriggerPython(Map<String, String> map, Map<String, String> mapNotes, String tablename, String flag) throws FileNotFoundException {
		Properties properties = readOrderedPropertiesFile("cache.properties");
		int i = 1;
		/**
		 * 创建触发函数头
		 */
		System.out.println("# -*- coding: utf-8 -*-");
		System.out.println("from base import FieldCalculation");
		System.out.println("from util.iapws_if97 import seuif97");
		System.out.println();
		System.out.println();
		/**
		 * 创建触发函数体
		 */
		Map<String, String> kkkmap = new HashMap<String, String>();
		for (String key : properties.stringPropertyNames()) {
			if (properties.getProperty(key).split("=").length > 1) {
				String right = properties.getProperty(key).split("=")[0];
				if (mapNotes.get(right).startsWith("特殊处理部分--")) {
					gzdih(properties.getProperty(key).split("=")[1], map, kkkmap, mapNotes, properties.getProperty(key).split("=")[0], i, flag, tablename);
					i += 1;
				}

			}

		}

		System.out.println("val = {");
		System.out.println("            'flg': 'design',");

		for (String str : kkkmap.keySet())
			System.out.println("            '" + str + "': form.get('" + str + flag + "'),");
		System.out.println("            'dbresult': oldobj}");
		System.out.println("        self.creatSubscriber(val)");
		System.out.println("        return val['dbresult']");
	}

	public static String captureName(String name) {
		name = name.substring(0, 1).toUpperCase() + name.substring(1);
		return name;

	}

	/**
	 * 实现特殊处理类
	 * @param str
	 * @param map
	 * @param strright
	 */
	public static void gzdih(String str, Map<String, String> map, Map<String, String> kkkmap, Map<String, String> mapNotes, String strright, int i, String fg, String tablename) {
		String[] arrSt = str.split("\\*|/|\\(|\\)|\\+|\\-|,");
		//将arrSt排序：由大到小
		System.out.println("# 实现字段" + strright + ":" + mapNotes.get(strright) + ",的计算" + i + "");
		System.out.println("class " + captureName(strright) + "(FieldCalculation):");
		System.out.println("    def notify(self, val):");
		System.out.println("        result = val['dbresult']");
		String dddString = "        if ";
		String str_sj = str;
		Set set_sj = new TreeSet();
		for (String str1 : arrSt) {
			if (str1.startsWith("MM")) {
				set_sj.add(str1);
			}
		}
		String[] arrSt_sj = (String[]) set_sj.toArray(new String[0]);
		for (String str1 : arrSt_sj) {
			String sead = map.get(str1) + fg + "";
			if (str1.equals(arrSt_sj[arrSt_sj.length - 1])) {
				dddString += "val['" + sead + "'] != '' and val['" + sead + "'] is not None";
			} else {
				dddString += "val['" + sead + "'] != '' and val['" + sead + "'] is not None and ";
			}
		}

		dddString += " :";
		System.out.println(dddString);
		//生成公式
		sort(arrSt_sj, "MM");
		for (String str1 : arrSt_sj) {
			kkkmap.put(map.get(str1), "");
			str_sj = str_sj.replaceAll(str1, "float(val['" + map.get(str1) + fg + "'])");
		}
		System.out.println("            " + strright + " = " + str_sj + "");
		System.out.println("            if " + strright + " >= 0:");
		System.out.println("                if val['flg'] == 'design':");
		System.out.println("                    result." + strright + fg + " = " + strright + "");
		System.out.println("                elif val['flg'] == 'check':");
		System.out.println("                    result." + strright + "_check = " + strright + "");
		System.out.println("        print(result)");
		System.out.println();
		System.out.println();
	}

	/**
	 * 由大到小排序
	 * @param num
	 */
	public static void sort(String[] num, String excleColumn) {
		int j = 0;
		while (j < num.length) {
			for (int i = 0; i < num.length - 1; i++) {
				if (Integer.parseInt(num[i].split(excleColumn)[1]) < Integer.parseInt(num[i + 1].split(excleColumn)[1])) {
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
	 * 由大到小排序
	 * @param num
	 */
	public static void sort1(String[] num) {
		int j = 0;
		while (j < num.length) {
			for (int i = 0; i < num.length - 1; i++) {
				if (Integer.parseInt(num[i].split("MM")[1]) < Integer.parseInt(num[i + 1].split("MM")[1])) {
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

	/*********************************************************生成常量******************************************************************/

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

