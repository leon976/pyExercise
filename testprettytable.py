from prettytable import PrettyTable

table = PrettyTable()

table.field_name = ["Name", "Age", "city"]

table.add_row(["alice",30,"miri"])
table.add_row(["bob",30,"kuching"])
table.add_row(["charlie",30,"paris"])

print (table)