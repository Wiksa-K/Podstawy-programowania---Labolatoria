using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programowanie.Entities
{
    public class Student
    {
        public Student(string fullname, int age, string phonenumber)
        {
            FullName = fullname;
            Age = age;
            PhoneNumber = phonenumber;
            Courses = new List<Course>();
            
            TutionFees = new List<TutionFee>();

            TutionFees.Add(new TutionFee(940,false, DateTime.Now.AddMonths(-3)));
            TutionFees.Add(new TutionFee(940, false, DateTime.Now.AddMonths(-2)));
            TutionFees.Add(new TutionFee(940, false, DateTime.Now.AddMonths(-1)));
            TutionFees.Add(new TutionFee(940, false, DateTime.Now));
            TutionFees.Add(new TutionFee(940, false, DateTime.Now.AddMonths(1)));

            Status = StudentStatus.Active;
        }

        public StudentStatus Status { get; set; }

        private void SetStatusGraduated()
        {
            bool hasNotCompletedCourses = Courses.Any(x => x.Grade <= 2);
            bool hasPaidAllTutions = TutionFees.Any(x => x.IsPaid == false);

            if (hasNotCompletedCourses == false && hasPaidAllTutions == false)
            {
                Status = StudentStatus.Graduated;
            }
        }

        public string FullName { get; set; }

        public int Age { get; set; }

        public string PhoneNumber { get; set; }

        public List<Course> Courses { get; set; }

        public StudentAddress Address { get; set; }

        public void AddCourse(int id, string name)
        {
            Courses.Add(new Course(id, name));
        }

        public void AddGrade(int courseId, int grade)
        {
            Course course = Courses.Single(x => x.Id == courseId);
            course.AddGrade(grade);
            SetStatusGraduated();
        }

        public List<TutionFee> TutionFees { get; set; }

        public void Pay(decimal amount)
        {
          var tution = TutionFees.Where(x => x.IsPaid == false).OrderBy(x => x.DueDate).FirstOrDefault();

            if (tution != null && tution.Amount == amount)
            {
                tution.Pay();
                SetStatusGraduated();
            }
        }
    }
}
