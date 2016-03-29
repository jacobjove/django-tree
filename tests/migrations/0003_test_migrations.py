from django.db import migrations
from tree.fields import PathField
from tree.operations import CreateTreeTrigger, RebuildPaths


class Migration(migrations.Migration):
    dependencies = [
        ('tests', '0002_add_tmp_model'),
    ]

    operations = [
        migrations.AddField('Something', 'path', PathField(null=True)),
        CreateTreeTrigger('Something', order_by=('name',)),
        RebuildPaths('Something'),
        migrations.AlterField('Something', 'path', PathField()),
        migrations.DeleteModel('Something'),
    ]