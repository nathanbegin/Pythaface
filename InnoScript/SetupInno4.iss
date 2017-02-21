; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{FBA3765A-9186-45D2-9C71-7582ACC01B63}
AppName=Calculatrice Pythagore
AppVersion=1.1
;AppVerName=Calculatrice Pythagore 1.1
AppPublisher=Nathan Begin Software
AppPublisherURL=http://www.nathanbegin.xyz
AppSupportURL=http://www.nathanbegin.xyz
AppUpdatesURL=http://www.nathanbegin.xyz
DefaultDirName={pf}\CalculatricePythagore
DefaultGroupName=Calculatrice Pythagore
OutputDir=C:\Users\natha\Desktop\Pythagore\Executable
OutputBaseFilename=CalculatricePythagore_Setup_v1.1
SetupIconFile=C:\Users\natha\Desktop\Pythagore\Code\Logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\natha\Desktop\Pythagore\Code\dist\PythagoreGUI.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\Desktop\Pythagore\Code\dist\Logo.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\Desktop\Pythagore\Code\build\PythagoreGUI\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Calculatrice Pythagore"; Filename: "{app}\PythagoreGUI.exe"
Name: "{group}\{cm:UninstallProgram,Calculatrice Pythagore}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Calculatrice Pythagore"; Filename: "{app}\PythagoreGUI.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\PythagoreGUI.exe"; Description: "{cm:LaunchProgram,Calculatrice Pythagore}"; Flags: nowait postinstall skipifsilent
