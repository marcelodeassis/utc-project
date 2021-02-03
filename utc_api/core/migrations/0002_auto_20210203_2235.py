from django.db import migrations

def init_task_states(apps, schema_editor):
    TaskState = apps.get_model("core", "TaskState")
    db_alias = schema_editor.connection.alias
    TaskState.objects.using(db_alias).bulk_create([
        TaskState(name="DONE"),
        TaskState(name="PENDING"),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_task_states),
    ]
