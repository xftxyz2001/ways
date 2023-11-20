#!/bin/bash

# 列出所有提交的文件并排序
committed_files=$(git log --pretty=format: --name-only --diff-filter=A | sort -u)

# 列出工作目录中的所有文件，过滤掉.git目录，并去除文件路径前缀，并排序
# all_files=$(find . -type f -not -path "./.git/*" -exec sh -c 'echo "{}"' \; | sed 's|^\./||' | sort -u)
all_files=$(find . -type f -not -path "./.git/*" | sed 's|^\./||' | sort -u)

# 筛选出现在工作目录中不存在的文件
# missing_files=$(comm -23 <(echo "$committed_files" | tr '\n' '\0' | xargs -0 printf "%s\n") <(echo "$all_files" | tr '\n' '\0' | xargs -0 printf "%s\n"))
missing_files=$(comm -23 <(echo "$committed_files") <(echo "$all_files"))

# 如果有缺失的文件，则进行处理
if [ -n "$missing_files" ]; then
  # 将$missing_files转换为数组
  IFS=$'\n' read -r -d '' -a missing_files_array <<<"$missing_files"

  total_files=${#missing_files_array[@]}
  current_file=0

  # 逐个处理缺失的文件
  for file in "${missing_files_array[@]}"; do
    echo "Processing $((++current_file)) of $total_files: $file"
    git filter-branch --force --index-filter "git rm --cached --ignore-unmatch $file" --prune-empty --tag-name-filter cat -- --all
  done

  # 强制推送到远程仓库
  git push origin main --force # 这里的分支名可能需要修改
  # 清理
  rm -rf .git/refs/original/
  git reflog expire --expire=now --all
  git gc --prune=now
  git gc --aggressive --prune=now
fi

# 结束
echo "Done"
