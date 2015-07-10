#!/bin/bash

FILE=$1
SLUG=`grep 'Slug: ' $FILE| sed 's/Slug: \(.*\)/\1/g'` 
SLUG_REPLACE=`echo $SLUG|nkf --url-input`
sed -i.bk "s/$SLUG/$SLUG_REPLACE/g" $FILE
