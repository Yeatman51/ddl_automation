# DDL Automation Process
![honu logo](img/honumg_logo.jpg)

This README Documentation was created to convey the process used to automate the DDL fridge/freezer daily downloads. additionally this document will cover the continued support and backlog of the DDL Site download files sent to the Honu DDL email daily.

## Files included in this project:

### DDL Automation (Fridge/Freezer)
- zone_1_ddl_automation
- zone_1_ddl_renaming

### DDL Email Download File Naming
- remove_external_name
- rename_ddl_email_download

### Email Download Automation Macros
- Download Attachment name from Email Subject
- Download Attachment name from Email Body Text
- Download Attachment name from Email file Name
- Download Attachment name from Email file Name and Subject

---

<div style="page-break-after: always;"></div>

# zone_1_ddl_automation
 Run this file to automatically launch log in search and download all DDL reports for LDC Fridge 10, Fridge 11, Fridge 12 and Freezer 18. All files will then automatically be downloaded into the downloads folder.

 ![](img/Screenshot_0001.png)

 ---
 ![](img/Screenshot_0002.png)

 ---
 ![](img/Screenshot_0003.png)

 ---


# zone_1_ddl_renaming
 After running the previous file the refrigerator renaming file will then automatically rename the last four files in your downloads folder in the order they were downloaded to the appropriate responding refrigerator or freezer name.

# remove_external_name
 A large number of files were sent with a non company or external e-mail address Because of this many of the files will be saved similar to the example below 

<div style="text-align:center">
 '[External] 220429 Jefferson Barnes PEDS'
</div>
<br>

 Running this file will remove the '[External]' Section of the file.

 <div style="text-align:center">
 '220429 Jefferson Barnes PEDS'
</div>
<br>

 This script is directly targeted at 'S:\Scans\DDL Email Download' and will remove '[External]' from every file inside of the DDL Email Download folder 

 If you run into an error it is because the file is removing the external portion and there is a file already named with an identical name. This is an easy fix simply rename the matching file something different and a rerun the script

# rename_ddl_email_download 
 Many files were not sent with the correct format or the corresponding site name and as a result have been downloaded with their default settings.

<div style="text-align:center">
 'DDL 113 2022-04-10 19_29_36 EST (Data EST).pdf'
</div>
<br>

 Running this file will remove the excess information and place the date at the beginning so all files can still be sorted by operational date 
 (see example below)

<div style="text-align:center">
 '220410 DDL 113'
</div>
<br>

 This script is directly targeted at 'S:\Scans\DDL name split' and will reformat every file inside of the DDL name split folder

 After running this file be sure to remove all of the renamed files and. Do not re run this file again as it will restructure anything inside of the DDL name split folder. Only rerun this file if every single file inside of DDL name split folder Has the original downloaded format.
 'DDL 113 2022-04-10 19_29_36 EST (Data EST).pdf'

# Email Download Automation Macros

## Download Attachment name from Email Subject
## Download Attachment name from Email Body Text
## Download Attachment name from Email file Name
## Download Attachment name from Email file Name and Subject

The following files represent custom VBA code that was used to generate a custom macro commands within the DDL email.

These macros are only accessible on the Outlook desktop application And you must be logged in to the DDL Email account

To execute the macro simply select the emails you wish to automatically download attachments from and then select which macro he would like to run

All of the files will be saved to the same location S:\Scans\DDL Email Download' Except the download by file name command. This command will save the selected email attachments directly to the to the name split folder 'S:\Scans\DDL name split'