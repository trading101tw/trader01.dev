#!/bin/bash
git init
git add .

git commit -m "submit" 
git branch -M main
git remote add origin git@github.com:trading101tw/trader01.git
git push -u origin main
