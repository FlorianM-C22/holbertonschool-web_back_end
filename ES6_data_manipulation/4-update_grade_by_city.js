export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.map((student) => {
    if (student.location === city) {
      const gradeObj = newGrades.find((grade) => grade.id === student.id);
      if (gradeObj) {
        return { ...student, grade: gradeObj.grade };
      }
    }
    return student;
  });
}
