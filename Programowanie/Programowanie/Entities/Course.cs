using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programowanie.Entities
{
    public class Course
    {
        public Course(int id, string name)
        {
            Name = name;
            Grade = 2;
            Id = id;
        }

        public int Id { get; set; }

        public void AddGrade(int grade)
        {
            Grade = grade;
        }

        public string Name { get; set; }

        public int Grade { get; set; }
    }
}
