class Person:
    def _init_(self):
        self._name = None
        self._job = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            # Convert the name to title case before saving
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

# List of approved jobs
APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

# Example usage:
# Create an instance of the Person class and set name and job
person = Person()
person.name = "john smith"
person.job = "ITC"
