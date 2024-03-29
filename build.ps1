$exclude = @("venv", "AutomateStar.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "AutomateStar.zip" -Force