created_date = '2025-01-10'
issue_date = '2025-02-20'

temp_created_date = created_date.split('-')[1] + '-' + created_date.split('-')[2]
temp_issue_date = issue_date.split('-')[1] + '-' + issue_date.split('-')[2]

print("Created date:", temp_created_date)
print("Issue date:", temp_issue_date)
    