Write-Host ""
Write-Host "Initial markdown generation..."
Write-Host ""

python scripts/generate_docs.py

Write-Host ""
Write-Host "Starting YAML watcher..."
Write-Host ""

Start-Process powershell -ArgumentList "-NoExit", "-Command", "python scripts/watch_and_generate.py"

Write-Host ""
Write-Host "Starting MkDocs server..."
Write-Host ""

python -m mkdocs serve