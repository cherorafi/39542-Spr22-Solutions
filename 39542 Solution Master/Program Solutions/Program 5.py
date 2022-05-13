"""
Name: Susan Sun
Email: susan.sun@hunter.cuny.edu
Resources:  https://www.textbook.ds100.org/ch/12/text_regex.html https://www.textbook.ds100.org/ch/12/text_re.html
"""

import re


def parse_date_from_one_line_log(file_name) -> str:
    date_regex = r"\d{4}-\d{2}-\d{2}"
    with open(file_name) as f:
        log_content = f.read()
        # print(log_content)
        log_date = re.findall(date_regex, log_content)[0]
    # print(log_date, type(log_date))
    return log_date

# log_date = parse_date_from_one_line_log('one_liner_log.txt')
# print(log_date, type(log_date))


def parse_min_max_date_from_one_line_logs(file_name):
    date_regex = r"\d{4}-\d{2}-\d{2}"
    with open(file_name) as f:
        log_content = f.read()
        parsed_date = re.findall(date_regex, log_content)
        # print(min(re.findall(date_regex, log_content)))
    min_log_date = min(parsed_date)
    max_log_date = max(parsed_date)
    # print(min_log_date, max_log_date)
    return min_log_date, max_log_date

# min_log_date, max_log_date = parse_min_max_date_from_one_line_logs('multi_liner_log.txt')
# print(min_log_date, type(min_log_date))
# print(max_log_date, type(max_log_date))


def parse_missing_filename_from_one_line_log(file_name) -> str:
    filename_regex = r"(?<=No such file or directory: ')(.*)(?=')"
    with open(file_name) as f:
        log_content = f.read()
        missing_filename = re.findall(filename_regex, log_content)[0]
    # print(re.findall(filename_regex, log_content))
    # print(log_missing_filename, type(log_missing_filename))
    return missing_filename

# missing_filename = parse_missing_filename_from_one_line_log('one_liner_log.txt')
# print(missing_filename, type(missing_filename))


def parse_filepath_linenum_from_traceback_log(file_name):
    filepath_regex = r'(?<=: File ")(.*)(?=")'
    line_regex = r"(?<=line )(.*)(?=, in )"
    with open(file_name) as f:
        log_content = f.read()
        log_content = log_content.replace('\n', ' ')
        log_content = re.sub(' +', ' ', log_content)
    log_filepath = re.findall(filepath_regex, log_content)[0]
    log_linenum = int(re.findall(line_regex, log_content)[0])
    # print(log_filepath, type(log_filepath), log_linenum, type(log_linenum))
    return log_filepath, log_linenum

# log_filepath, log_linenum = parse_filepath_linenum_from_traceback_log('traceback_log_simple.txt')
# print(log_filepath)
# print(log_linenum)


def parse_last_linenum_from_traceback_log(file_name) -> int:
    line_regex = r"(?<=line ).*?(?=, in)"
    with open(file_name) as f:
        log_content = f.read()
        log_content = log_content.replace('\n', ' ')
        log_content = re.sub(' +', ' ', log_content)
        # print(log_content)
    log_linenum = re.findall(line_regex, log_content)
    # print(log_linenum, type(log_linenum))
    last_linenum = int(log_linenum[len(log_linenum) - 1])
    # print(last_linenum, type(last_linenum))
    return last_linenum

# last_linenum = parse_last_linenum_from_traceback_log('traceback_log_complex.txt')
# print(last_linenum, type(last_linenum))
