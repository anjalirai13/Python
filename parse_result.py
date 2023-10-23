import xml.etree.ElementTree as ET
import os
import re

def parse_result(log_file):
    xml_tree = ET.parse(log_file)
    root = xml_tree.getroot()
    csv_file = log_file.replace(".xml", ".csv")
    file = open(csv_file, "w")
    file.write("Name,Result,ReturnCode,Error,Function,Logs\n")
    fd = open(log_file.replace(".xml", ".txt"), "w")
    for items in root:
        child_sysout = ""
        tc_name = items.attrib["name"]
        spattern = re.compile("(.*)Function not implemented(.*)")
        child = items.find("properties")
        error_str = items.find("error")
        skipped = items.find("skipped")
        returncode = 0
        func = ""
        res = "Not Defined"
        if skipped is None:
            if child is not None:
                if items.find("system-out").text is not None:
                    child_sysout = items.find("system-out").text
                else:
                    child_sysout = None
                c_prop = child.find("property")
                returncode = c_prop.attrib["value"]
                if child_sysout is not None:
                    if "ENOSYS" in child_sysout and "Failed to acquire device" in child_sysout:
                        res = "FAIL"
                        error_str = "ENOSYS and Failed to acquire device"
                        func = re.search(spattern, child_sysout)
                    elif "Failed to acquire device" in child_sysout:
                        res = "FAIL"
                        error_str = "Failed to acquire device"
                    elif "ENOSYS" in child_sysout or "Function not implemented" in child_sysout:
                        res = "FAIL"
                        error_str = "ENOSYS"
                        func = re.search(spattern, child_sysout)
                else:
                    res = "FAIL"
            elif error_str is not None:
                error_str = error_str.text
                res = "Timeout"
                fd.write("{} {}\n".format(tc_name, tc_name))
        else:
            res = "skipped"

        if func is None or func == "":
            func = ""
        else:
            func = func.group()
        file.write("{},{},{},{},{},{}\n".format(tc_name, res, returncode, error_str, func, child_sysout.replace("\n", ". ").replace(",", " ")))

    file.close()
    fd.close()

log_path = "C:\Users\\Documents\\"
file_name = "test_logs_120.xml"

log_file = os.path.join(log_path, file_name)
parse_result(log_file)