Attribute VB_Name = "Module5"

Sub SpecialCharactersSubjectAttachments()
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
 
FolderPath = "S:\Scans\DDL Email Download"
 
  
Set OutlookApp = Outlook.Application
Set Selection = OutlookApp.ActiveExplorer.Selection 'Determine what emails are selected
 
AttachmentsCount = 0 'Track how many Attachments are saved
 
For Each Email In Selection
Set Attachments = Email.Attachments
For i = Attachments.Count To 1 Step -1
'If InStr(1, Attachments.Item(i).Filename, "File Type Extension") > 1 Then 'Check File Type before saving
Attachments.Item(i).SaveAsFile FolderPath & "\" & AllowedChars(Email.Subject) & ".pdf"
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

Private Function AllowedChars(ByRef s As String) As String
   Dim i As Long
   Dim myChar As String
   AllowedChars = s
   For i = 1 To Len(AllowedChars)
       myChar = Mid$(AllowedChars, i, 1)
       If myChar Like "[<>:""/\|?*]" Or Asc(myChar) < 32 Then
           Mid$(AllowedChars, i, 1) = "_"
       End If
   Next i
End Function

