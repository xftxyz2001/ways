New-Alias -Name git -Value "C:\Program Files\Git\bin\git.exe"
Import-Module posh-git
Import-Module oh-my-posh
Set-Theme Paradox

# Shows navigable menu of all options when hitting Tab
Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete

# Autocompletion for arrow keys
Set-PSReadLineKeyHandler -Key UpArrow -ScriptBlock {
    [Microsoft.PowerShell.PSConsoleReadLine]::HistorySearchBackward()
    [Microsoft.PowerShell.PSConsoleReadLine]::EndOfLine()
}
Set-PSReadLineKeyHandler -Key DownArrow -ScriptBlock {
    [Microsoft.PowerShell.PSConsoleReadLine]::HistorySearchForward()
    [Microsoft.PowerShell.PSConsoleReadLine]::EndOfLine()
}

# auto suggestions
Import-Module PSReadLine
$supportsVirtualTerminal = $null -ne $Host.UI.PSObject.Properties['SupportsVirtualTerminal'] -and
    $Host.UI.SupportsVirtualTerminal
$canShowPredictions = $Host.Name -eq 'ConsoleHost' -and
    -not [Console]::IsInputRedirected -and
    -not [Console]::IsOutputRedirected -and
    $supportsVirtualTerminal

if ($canShowPredictions) {
    Set-PSReadLineOption -PredictionSource HistoryAndPlugin
    Set-PSReadLineOption -PredictionViewStyle ListView
}
