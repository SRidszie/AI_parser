import random

class DepartmentTitleGenerator:
    def __init__(self):
        self.departments = {
            'IT': ['Software Engineer', 'Data Scientist', 'DevOps Engineer', 'IT Consultant', 'Cybersecurity Analyst'],
            'Sales': ['Sales Executive', 'Sales Manager', 'Business Development Executive', 'Account Manager'],
            'Marketing': ['Marketing Coordinator', 'Digital Marketing Specialist', 'Marketing Manager', 'SEO Specialist'],
            'Finance': ['Financial Analyst', 'Accountant', 'Financial Controller', 'Investment Analyst'],
            'Human Resources': ['HR Executive', 'HR Manager', 'Recruitment Specialist', 'Training Coordinator'],
            'Operations': ['Operations Manager', 'Supply Chain Analyst', 'Logistics Coordinator', 'Quality Assurance Manager'],
            'Customer Service': ['Customer Service Representative', 'Customer Success Manager', 'Call Center Supervisor'],
            'Research and Development': ['Research Scientist', 'Product Development Engineer', 'Innovation Manager']
        }

    def generate_title(self, department):
        """
        Generate a job title for the given department.

        Args:
        - department (str): The department for which a job title is to be generated.

        Returns:
        - str: A randomly chosen job title for the given department.
        """
        if department in self.departments:
            return random.choice(self.departments[department])
        else:
            return "Department not found"

if __name__ == "__main__":
    generator = DepartmentTitleGenerator()
    
    print("Sample Department Titles:")
    print("--------------------------")
    for department in generator.departments:
        title = generator.generate_title(department)
        print(f"{department}: {title}")
