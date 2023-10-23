import os
import csv
from selenium import webdriver


class TEST_CONFIG:
    def __init__(self):
        self.benchmark_result = []
        self.test_scenario = "cpu"
        self.result_path = "results"


class Geekbench:
    def __init__(self):
        pass

    def filter_data(self, name, benchmark_result):
        logs = []
        for b_logs in benchmark_result:
            for k, v in b_logs.items():
                if k == name:
                    logs.append(v)
        return logs

    def parse_results(self, TEST_CONFIG):
        logs_dir = "C:\\Validation\\logs"
        test_details = {}
        for mode in ["baseline", "testapp"]:
            workload_file_path = os.path.join(logs_dir, TEST_CONFIG.result_path, TEST_CONFIG.test_name, mode)
            with open(os.path.join(workload_file_path, "workloadData.txt"), "r") as data:
                data = data.readlines()
                for line in data:
                    if "https://browser.geekbench.com/" in line:

                        driver_value = None
                        chrome_options = webdriver.ChromeOptions()
                        prefs = {"profile.default_content_setting_values.notifications": 2}
                        chrome_options.add_experimental_option("prefs", prefs)
                        chrome_driver_path = 'C:\\VALIDATION\\tools\\'
                        driver = webdriver.Chrome(chrome_options=chrome_options)

                        # driver = webdriver.Chrome()
                        driver.get(line.strip())
                        scenario = TEST_CONFIG.test_scenario
                        element_xpath = "/html/body/div/div/div[1]/div[3]/div"
                        k_name = str(driver.find_element_by_xpath(element_xpath + "[1]/div[2]").text)
                        value = int(driver.find_element_by_xpath(element_xpath + "[1]/div[1]").text)

                        test_details[k_name] = test_details[k_name] + [value] if test_details.get(k_name) else [value]

                        if "cpu" in scenario:
                            k_name = str(driver.find_element_by_xpath(element_xpath + "[2]/div[2]").text)
                            value = int(driver.find_element_by_xpath(element_xpath + "[2]/div[1]").text)
                            test_details[k_name] = test_details[k_name] + [value] if test_details.get(k_name) else [
                                value]

                        driver.close()
                        break
        TEST_CONFIG.benchmark_result.append(test_details)

        if TEST_CONFIG.performance_calculate:
            self.calculate_performance(TEST_CONFIG)

    def calculate_performance(self, TEST_CONFIG):
        benchmark_result = TEST_CONFIG.benchmark_result
        file_path = os.path.join(TEST_CONFIG.result_path,
                                 'geekbench5_{}_analysis.csv'.format(TEST_CONFIG.test_scenario))
        print(file_path)
        with open(file_path, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(["Benchmark", "Baseline", "TestApp", "Degradation %"])
            benchmark_list = []
            for results in benchmark_result:
                benchmark_list += (list(results.keys()))

            for name in list(set(benchmark_list)):
                results = self.filter_data(name, benchmark_result)
                min_degradation = max_degradation = min_row = max_row = ''
                degradation_list = []
                for score in results:
                    degradation = ((score[0] - score[1]) / score[0]) * 100
                    degradation_list.append(degradation)
                    writer.writerow([name, score[0], score[1], degradation])
                    if min_degradation == "" and max_degradation == "":
                        min_degradation = max_degradation = degradation
                        min_row = max_row = score
                    if min_degradation > degradation:
                        min_degradation = degradation
                        min_row = score
                    if max_degradation < degradation:
                        max_degradation = degradation
                        max_row = score
                [results.remove(val) for val in [min_row, max_row]]
                [degradation_list.remove(val) for val in [min_degradation, max_degradation]]
                baseline_logs = [val[0] for val in results]
                testapp_logs = [val[1] for val in results]
                baseline_mean = sum(baseline_logs) / len(baseline_logs)
                testapp_mean = sum(testapp_logs) / len(testapp_logs)
                degradation_mean = sum(degradation_list) / len(degradation_list)
                writer.writerow([])
                writer.writerow(["Centered Average", baseline_mean, testapp_mean, degradation_mean])
                writer.writerow([])


test_config = TEST_CONFIG()
gk = Geekbench()
folders = ["geekbench5_cpu_iteration_0",
           "geekbench5_cpu_iteration_1",
           "geekbench5_cpu_iteration_2",
           "geekbench5_cpu_iteration_3",
           "geekbench5_cpu_iteration_4"]
for dirs in folders:
    test_config.test_name = dirs
    if "test_win_cj_perf_geekbench5_cpu_iteration_4" in dirs:
        test_config.performance_calculate = True
    gk.parse_results(test_config)