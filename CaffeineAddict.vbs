Set WshShell = WScript.CreateObject("WScript.Shell")

a = InputBox("Enter time to Caffeinate","Enter Value",10)
msgbox "Enjoy A Cup of Joe!!!!!"

WScript.Sleep 1000

WshShell.Run "%windir%\notepad.exe"
WshShell.AppActivate "Notepad"


Do While i < a*6
	WshShell.AppActivate "Notepad"
	WshShell.SendKeys(i)
	WshShell.SendKeys "{ENTER}"
	WScript.Sleep 10000 ' time in millisecond
	i = i + 1
	
Loop
msgbox "completed the time now Decaffeinating !!!"