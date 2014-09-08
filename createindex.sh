#!/bin/bash

cd `dirname $0`

function _list () {
	target="$1"
	index="$target/__init__.py"
	rm -f "$index"
	
	all=$(
		ls -1 "$target" | while read f; do
			if [[ "$f" =~ \.py$ ]] && [ "$f" != "__init__.py" ]; then
				module=`echo $target | sed 's|/|.|g'`
				clazz=$( grep "^class " "$target/$f" | cut -d" " -f2 | sed 's/[^a-zA-Z0-9_].*//' )
				echo "from .${f%.py} import $clazz # NOQA" >> "$index"
				echo -n ", '$clazz'"
			fi
		done
	)
	echo >> "$index"
	echo "__all__ = [" >> "$index"
	echo "$all" | sed 's/^,/   /' >> "$index"
	echo "]" >> "$index"
	
	ls -1 "$target" | while read f; do
		if [ -d "$target/$f" ]; then
			_list "$target/$f" &
		fi
	done
}

#_list "saklient"
