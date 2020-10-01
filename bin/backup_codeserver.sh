codeserver=root@192.168.8.250
remote_path=/home/git-data/repositories/
repos=`ssh $codeserver "find $remote_path -name "*.git""`
echo "repos=$repos"
for repo in $repos
do
	echo "repo=$repo"
	name=`basename $repo`
	echo "name=$name"
	if [ ! -d $name ];then
		git clone --bare $codeserver:$repo $name
	else
		cd $name
		git fetch --all
		cd ..
	fi
done
