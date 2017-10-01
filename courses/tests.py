from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Course
from .models import Step

# Create your tests here.


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)
        # assets arg1 < arg2


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python Testing',
            description='Learn to test in python'
        )
        self.course2 = Course.objects.create(
            title='New Course',
            description='A new course'
        )
        self.step = Step.objects.create(
            title='Introduction to Doctests',
            description='Learn to write doc tests',
            course=self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:course_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        # template tests
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:course_detail', kwargs={'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step_detail', kwargs={
                'course_pk': self.course.pk,
                'step_pk': self.step.pk}))
        self.assertEqual(resp.status_code, 200)





