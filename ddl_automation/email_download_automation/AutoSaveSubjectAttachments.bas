Attribute VB_Name = "Module4"
Sub AutoSaveSubjectAttachments()
' Means variable is in use
Dim Attachments As Outlook.Attachments '
Dim AttachmentsCount As Integer '
Dim Email As Outlook.MailItem '
Dim FolderObj As Object '
Dim FolderPath As String '
Dim i As Long '
Dim OutlookApp As Outlook.Application '
Dim Selection As Outlook.Selection
Dim User As String '
  
On Error GoTo HelpError
 
User = (Environ$("Username")) 'Identify Username
FolderPath = "S:\Scans\DDL Email Download"
 
Set FolderObj = CreateObject("Scripting.FileSystemObject")
If FolderObj.FolderExists(FolderPath) Then 'The Folder has been found
Else: FolderObj.CreateFolder (FolderPath) 'The Folder has been created
End If
  
Set OutlookApp = Outlook.Application
Set Selection = OutlookApp.ActiveExplorer.Selection 'Determine what emails are selected
 
AttachmentsCount = 0 'Track how many Attachments are saved
 
For Each Email In Selection
'If Email.SenderEmailAddress = "" Or Email.Categories = "" Or Email.Subject = "" Or InStr(1, Email.Subject, "Search for Text") > 1 Then
Set Attachments = Email.Attachments
For i = Attachments.Count To 1 Step -1
'If InStr(1, Attachments.Item(i).Filename, "File Type Extension") > 1 Then 'Check File Type before saving
Attachments.Item(i).SaveAsFile FolderPath & "\" & Format(Email.Subject, "") & ".pdf" 'Save attachment to the Folder Path using naming convention: Email's Received Time - Attachment's File Name
AttachmentsCount = AttachmentsCount + 1
'End If
Next i
'End If
Next
 
If AttachmentsCount > 0 Then
MsgBox "Email Attachment(s) have been saved to the Attachments folder."
ElseIf AttachmentsCount = 0 Then
MsgBox "No Email Attachment(s) were found to save."
End If
 
Set Attachments = Nothing
Set Email = Nothing
Set FolderObj = Nothing
Set OutlookApp = Nothing
Set Selection = Nothing
 
Exit Sub
 
HelpError:
MsgBox (Err.Number & " - " & Err.Description & vbNewLine & vbNewLine & "HELP")
   
End Sub



