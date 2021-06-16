def analyzefile():
    member_validate = open("app_common.py", 'r')
    total_line_count = 0
    empty_line_count = 0
    comments_count = 0
    for line in member_validate:
        total_line_count = total_line_count + 1
        if line in ['\n', '\r\n']:
            empty_line_count = empty_line_count + 1
        if "#" in line or "'''" in line:
            comments_count = comments_count + 1

    noncoomer_validate = open("app_defines.py", 'r')
    noncommer_line_count = 0
    noncommer_empty_line_count = 0
    noncommer_comments_count = 0
    for line in noncoomer_validate:
        noncommer_line_count = noncommer_line_count + 1
        if line in ['\n', '\r\n']:
            noncommer_empty_line_count = noncommer_empty_line_count + 1
        if "#" in line or "'''" in line:
            noncommer_comments_count = noncommer_comments_count + 1

    appdefine_validate = open("app_thread.py", 'r')
    appdefine_line_count = 0
    appdefine_emptyline_count = 0
    appdefine_count = 0
    for line in appdefine_validate:
        appdefine_line_count = appdefine_line_count + 1
        if line in ['\n', '\r\n']:
            appdefine_emptyline_count = appdefine_emptyline_count + 1
        if "#" in line or "'''" in line:
            appdefine_count = appdefine_count + 1

    datetimefile_validate = open("dateTime_operation.py", 'r')
    datetimefile_line_count = 0
    datetimefile_emptyline_count = 0
    datetimefile_count = 0
    for line in datetimefile_validate:
        datetimefile_line_count = datetimefile_line_count + 1
        if line in ['\n', '\r\n']:
            datetimefile_emptyline_count = datetimefile_emptyline_count + 1
        if "#" in line or "'''" in line:
            datetimefile_count = datetimefile_count + 1

    mondontaonstatement_validate = open("Inventory_Main.py", 'r')
    mondontaonstatement_line_count = 0
    mondontaonstatement_emptyline_count = 0
    mondontaonstatement_count = 0
    for line in mondontaonstatement_validate:
        mondontaonstatement_line_count = mondontaonstatement_line_count + 1
        if line in ['\n', '\r\n']:
            mondontaonstatement_emptyline_count = mondontaonstatement_emptyline_count + 1
        if "#" in line or "'''" in line:
            mondontaonstatement_count = mondontaonstatement_count + 1

    initdatabase_validate = open("Inventory_Entry.py", 'r')
    initdatabase_line_count = 0
    initdatabase_emptyline_count = 0
    initdatabase_count = 0
    for line in initdatabase_validate:
        initdatabase_line_count = initdatabase_line_count + 1
        if line in ['\n', '\r\n']:
            initdatabase_emptyline_count = initdatabase_emptyline_count + 1
        if "#" in line or "'''" in line:
            initdatabase_count = initdatabase_count + 1

    appthread_validate = open("inventory_report.py", 'r')
    appthread_line_count = 0
    appthread_emptyline_count = 0
    appthread_count = 0
    for line in appthread_validate:
        appthread_line_count = appthread_line_count + 1
        if line in ['\n', '\r\n']:
            appthread_emptyline_count = appthread_emptyline_count + 1
        if "#" in line or "'''" in line:
            appthread_count = appthread_count + 1

    stksales_validate = open("inventory_sales.py", 'r')
    stksalesline_count = 0
    stksalesempty_line_count = 0
    stksalescomments_count = 0
    for line in stksales_validate:
        stksalesline_count = stksalesline_count + 1
        if line in ['\n', '\r\n']:
            stksalesempty_line_count = stksalesempty_line_count + 1
        if "#" in line or "'''" in line:
            stksalescomments_count = stksalescomments_count + 1

    act_validate = open("merchandise.py", 'r')
    actline_count = 0
    actempty_line_count = 0
    actcomments_count = 0
    for line in act_validate:
        actline_count = actline_count + 1
        if line in ['\n', '\r\n']:
            actempty_line_count = actempty_line_count + 1
        if "#" in line or "'''" in line:
            actcomments_count = actcomments_count + 1


    stockInf_validate = open("user_account.py", 'r')
    stockInfline_count = 0
    stockInfempty_line_count = 0
    stockInfcomments_count = 0
    for line in stockInf_validate:
        stockInfline_count = stockInfline_count + 1
        if line in ['\n', '\r\n']:
            stockInfempty_line_count = stockInfempty_line_count + 1
        if "#" in line or "'''" in line:
            stockInfcomments_count = stockInfcomments_count + 1
            
    sales_validate = open("sales_report.py", 'r')
    salesline_count = 0
    salesempty_line_count = 0
    salescomments_count = 0
    for line in sales_validate:
        salesline_count = salesline_count + 1
        if line in ['\n', '\r\n']:
            salesempty_line_count = salesempty_line_count + 1
        if "#" in line or "'''" in line:
            salescomments_count = salescomments_count + 1
            
    customerDetails_validate = open("customer_details.py", 'r')
    customerDetailsline_count = 0
    customerDetailsempty_line_count = 0
    customerDetailscomments_count = 0
    for line in customerDetails_validate:
        customerDetailsline_count = customerDetailsline_count + 1
        if line in ['\n', '\r\n']:
            customerDetailsempty_line_count = customerDetailsempty_line_count + 1
        if "#" in line or "'''" in line:
            customerDetailscomments_count = customerDetailscomments_count + 1

    total = total_line_count + noncommer_line_count + appdefine_line_count + \
            datetimefile_line_count + mondontaonstatement_line_count + \
            initdatabase_line_count + appthread_line_count + stksalesline_count + actline_count \
            + stockInfline_count + salesline_count + customerDetailsline_count

    comments = comments_count + noncommer_comments_count + appdefine_count + \
               datetimefile_count + mondontaonstatement_count + \
               initdatabase_count + appthread_count + actcomments_count + stksalescomments_count \
                + salescomments_count + customerDetailscomments_count

    empty_lines = empty_line_count + noncommer_empty_line_count + \
                  appdefine_emptyline_count + \
                  datetimefile_emptyline_count + mondontaonstatement_emptyline_count + \
                  initdatabase_emptyline_count + appthread_emptyline_count + stksalesempty_line_count + actempty_line_count  \
                  + stockInfempty_line_count + salesempty_line_count + customerDetailsempty_line_count
    print("---------------------------------------------------")
    print("Total number of lines : ", total)
    print("Empty lines : ", empty_lines)
    print("Total comments : ", comments)
    print("\nUn-effective LOC : ", comments + empty_lines)
    print("Effective LOC : ", total - empty_lines - comments)
    print("---------------------------------------------------")


analyzefile()
import socket
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
