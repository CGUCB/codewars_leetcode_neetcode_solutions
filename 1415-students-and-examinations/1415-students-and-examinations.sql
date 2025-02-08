# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        st.student_id,
        st.student_name,
        su.subject_name
    FROM
        Students AS st
    CROSS JOIN
        Subjects AS su
    UNION ALL
    SELECT
        st.student_id,
        st.student_name,
        e.subject_name
    FROM
        Students AS st
    JOIN
        Examinations AS e
    ON
        e.student_id = st.student_id
)
SELECT
    student_id,
    student_name,
    subject_name,
    COUNT(*) - 1 AS attended_exams
FROM
    CTE
GROUP BY
    student_id,
    student_name,
    subject_name
ORDER BY
    student_id ASC,
    subject_name ASC