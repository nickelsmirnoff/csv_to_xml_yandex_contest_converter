import csv

input_file_name = "input.csv"
output_file_name = "output.xml"
print("reading from",input_file_name)

with open(input_file_name, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file)
    file_writer = open(output_file_name,"w")
    col_names = file_reader.__next__()
    print(col_names)
    file_writer.write("<ValCurs Data=\"01.01.2021\" name=\"Foreign Currency Market\">")
    string_format = "<Valute ID=\"{0}\"><NumCode>{1}</NumCode><CharCode>{2}</CharCode><Nominal>{3}</Nominal><Name>{4}</Name><Value>{5}</Value></Valute>"
    for row in file_reader:
        file_writer.write(string_format.format(row[1], row[2], row[3], row[4], row[5], row[6]))
    file_writer.write("</ValCurs>")
    file_writer.close()