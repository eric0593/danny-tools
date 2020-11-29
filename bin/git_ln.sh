rm -rf config
ln -sf $1/config config
rm -rf description
ln -sf $1/description description
rm -rf hooks
ln -sf $1/hooks hooks
rm -rf info
ln -sf $1/info info
rm -rf logs
ln -sf $1/logs logs
rm -rf objects
ln -sf $1/objects objects
rm -rf packed-refs
ln -sf $1/packed-refs packed-refs
rm -rf refs
ln -sf $1/refs refs
rm -rf rr-cache
ln -sf $1/rr-cache rr-cache
rm -rf shallow
ln -sf $1/shallow shallow
rm -rf svn
ln -sf $1/svn svn
