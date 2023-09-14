
function getIP {

    (Get-NetIPAddress).ipv4address | Select-String "192*"

}

function getUser {

    $env:USERNAME
}

#Powershell version
$Version = $Host.Version.Major

#Name of PC
$PCname = hostname

#IP Address
$IP = getIP

#Type of User
$USER = getUser

$DATE = Get-Date -Format "dddd, MMMM dd, yyyy"

Set-ExecutionPolicy -ExecutionPolicy Unrestricted

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $PCName. PowerShell Version $Version. Today's date is $DATE." 

Write-Host($BODY)

Send-MailMessage -To "chopranl@mail.uc.edu" -From "excel.plasma@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)

