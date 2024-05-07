from django.core.management.base import BaseCommand
from assessment_app.models import AssessmentQuestionCollection, AssessmentQuestion

# Link to CSV in Drive:
# collection_name,question_section,question_text,question_help_text,question_type,order,required
# 

class Command(BaseCommand):
    help = 'Uploads assessment questions from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        # Read the CSV file and create assessment questions
        with open(csv_file, 'r') as file:
            # Assuming the CSV file has the following columns:
            # collection_name, question_section, question_text, question_type, order, required
            for line in file:
                data = line.strip().split(',')
                collection_name = data[0]
                question_section = data[1]
                question_text = data[2]
                question_type = data[3]
                order = int(data[4])
                required = True if data[5].lower() == 'true' else False

                # Get or create the assessment question collection
                collection, created = AssessmentQuestionCollection.objects.get_or_create(name=collection_name)

                # Create the assessment question
                AssessmentQuestion.objects.create(
                    collection=collection,
                    question_section=question_section,
                    question_text=question_text,
                    question_type=question_type,
                    order=order,
                    required=required
                )

        self.stdout.write(self.style.SUCCESS('Assessment questions uploaded successfully.'))