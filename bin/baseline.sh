mv .git ../
find . -name ".git" | xargs rm -rf 
rm -rf prebuilts tools
mv ../.git .
echo "git add -A"
git add -A
git status

