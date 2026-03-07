using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programowanie.Entities
{
    public class StudentStatus
    {
        public static StudentStatus Graduated { get; internal set; }
        public static StudentStatus Active { get; internal set; }
    }
}
