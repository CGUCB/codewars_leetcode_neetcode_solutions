SELECT
    *
FROM
    Users
WHERE
    mail REGEXP '^[A-Za-z][-\\w\\._]*@leetcode\\.com$'