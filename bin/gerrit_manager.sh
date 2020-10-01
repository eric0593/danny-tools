username=admin
local_host=127.0.0.1
basepath=codeaurora
set-gerrit-var(){
	username=$1
	local_host=$2
	basepath=$3
}

get-gerrit-var(){
	echo username=$username
	echo local_host=$local_host
	echo basepath=$basepath
}

ls-projects(){
	ssh -p 29418 $username@$local_host gerrit ls-projects
}

create-project(){
	echo "ssh -p 29418 $username@$local_host gerrit create-project $basepath/REPO_PROJECT"
}

set-project-parent(){
	echo "ssh -p 29418 $username@$local_host gerrit set-project-parent --parent $basepath/permission-base $basepath/REPO_PROJECT"
}

push-project(){
	echo "git push ssh://$username@$local_host:29418/$1 "refs/heads/*:refs/heads/*""
}

