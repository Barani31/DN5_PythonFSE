Department

DepartmentID (PK)
DepartmentName

        |

        | 1

        |

        | *

Course

CourseID (PK)

CourseName

DepartmentID (FK)

        |

        | *

        |

        | *

Enrollment

EnrollmentID

StudentID (FK)

CourseID (FK)

        |

        | *

        |

        | 1

Student

StudentID (PK)

StudentName