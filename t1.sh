if [-z $@]; then
    git add .
fi

if [-n $@]; then
    git add $@
fi

git commit -m "linux"
git push