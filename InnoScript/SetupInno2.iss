; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{428B0B45-AE76-4AB5-BCF8-17EA01AF330B}
AppName=CalculatricePythagore
AppVersion=2.0
;AppVerName=CalculatricePythagore 2.0
AppPublisher=BeginSoftware
AppPublisherURL=http://www.nathanbegin.xyz
AppSupportURL=http://www.nathanbegin.xyz
AppUpdatesURL=http://www.nathanbegin.xyz
DefaultDirName={pf}\CalculatricePythagore
DefaultGroupName=CalculatricePythagore
OutputDir=C:\Users\natha\Desktop
OutputBaseFilename=PythagoreCalculatrice_Setup_2.0.exe
SetupIconFile=B:\Documents\AUTRES\GIT\Pythagore\Logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\natha\Desktop\Pythagore\build\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\natha\Desktop\Pythagore\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\natha\Desktop\Pythagore\dist\Logo.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\Desktop\Pythagore\dist\PythagoreGUI.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\CalculatricePythagore"; Filename: "{app}\PythagoreGUI.exe"; Tasks: desktopicon
Name: "{commondesktop}\CalculatricePythagore"; Filename: "{app}\Logo.ico"

[Run]
Filename: "{app}\PythagoreGUI.exe"; Description: "{cm:LaunchProgram,CalculatricePythagore}"; Flags: nowait postinstall skipifsilent
