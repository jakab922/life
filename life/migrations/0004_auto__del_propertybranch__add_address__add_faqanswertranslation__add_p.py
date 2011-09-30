# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'PropertyBranch'
        db.delete_table('life_propertybranch')

        # Adding model 'Address'
        db.create_table('life_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('life', ['Address'])

        # Adding model 'FaqAnswerTranslation'
        db.create_table('life_faqanswertranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('faq', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Faq'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('answer_translation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('life', ['FaqAnswerTranslation'])

        # Adding model 'PropertyDescription'
        db.create_table('life_propertydescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('short_desc', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
        ))
        db.send_create_signal('life', ['PropertyDescription'])

        # Adding model 'Property'
        db.create_table('life_property', (
            ('property_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('parking', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tenure_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Address'])),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Branch'])),
        ))
        db.send_create_signal('life', ['Property'])

        # Adding model 'TestimonialTranslation'
        db.create_table('life_testimonialtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testimonial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Testimonial'])),
            ('langauge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('quote', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('life', ['TestimonialTranslation'])

        # Adding model 'PropertyThumbnail'
        db.create_table('life_propertythumbnail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('life', ['PropertyThumbnail'])

        # Adding model 'FaqTranslation'
        db.create_table('life_faqtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('faq', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Faq'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('life', ['FaqTranslation'])

        # Adding model 'Branch'
        db.create_table('life_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Address'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contact_person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.StaffMember'])),
        ))
        db.send_create_signal('life', ['Branch'])

        # Deleting field 'StaffMember.language'
        db.delete_column('life_staffmember', 'language_id')

        # Deleting field 'StaffMember.update_date'
        db.delete_column('life_staffmember', 'update_date')

        # Deleting field 'StaffMember.creation_date'
        db.delete_column('life_staffmember', 'creation_date')

        # Adding M2M table for field language on 'StaffMember'
        db.create_table('life_staffmember_language', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staffmember', models.ForeignKey(orm['life.staffmember'], null=False)),
            ('language', models.ForeignKey(orm['life.language'], null=False))
        ))
        db.create_unique('life_staffmember_language', ['staffmember_id', 'language_id'])

        # Deleting field 'Testimonial.quote'
        db.delete_column('life_testimonial', 'quote')

        # Deleting field 'Testimonial.id'
        db.delete_column('life_testimonial', 'id')

        # Adding field 'Testimonial.quote_name'
        db.add_column('life_testimonial', 'quote_name', self.gf('django.db.models.fields.CharField')(default='bubba', max_length=50, primary_key=True), keep_default=False)

        # Deleting field 'Faq.answer'
        db.delete_column('life_faq', 'answer')

        # Deleting field 'Faq.question'
        db.delete_column('life_faq', 'question')

        # Deleting field 'Faq.title'
        db.delete_column('life_faq', 'title')

        # Adding field 'Faq.name'
        db.add_column('life_faq', 'name', self.gf('django.db.models.fields.CharField')(default='asdf', max_length=50), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'PropertyBranch'
        db.create_table('life_propertybranch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('life', ['PropertyBranch'])

        # Deleting model 'Address'
        db.delete_table('life_address')

        # Deleting model 'FaqAnswerTranslation'
        db.delete_table('life_faqanswertranslation')

        # Deleting model 'PropertyDescription'
        db.delete_table('life_propertydescription')

        # Deleting model 'Property'
        db.delete_table('life_property')

        # Deleting model 'TestimonialTranslation'
        db.delete_table('life_testimonialtranslation')

        # Deleting model 'PropertyThumbnail'
        db.delete_table('life_propertythumbnail')

        # Deleting model 'FaqTranslation'
        db.delete_table('life_faqtranslation')

        # Deleting model 'Branch'
        db.delete_table('life_branch')

        # Adding field 'StaffMember.language'
        db.add_column('life_staffmember', 'language', self.gf('django.db.models.fields.related.ForeignKey')(default='uk', to=orm['life.Language']), keep_default=False)

        # Adding field 'StaffMember.update_date'
        db.add_column('life_staffmember', 'update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 9, 26), blank=True), keep_default=False)

        # Adding field 'StaffMember.creation_date'
        db.add_column('life_staffmember', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 9, 26), blank=True), keep_default=False)

        # Removing M2M table for field language on 'StaffMember'
        db.delete_table('life_staffmember_language')

        # Adding field 'Testimonial.quote'
        db.add_column('life_testimonial', 'quote', self.gf('django.db.models.fields.TextField')(default='bubba'), keep_default=False)

        # Adding field 'Testimonial.id'
        db.add_column('life_testimonial', 'id', self.gf('django.db.models.fields.AutoField')(default=13, primary_key=True), keep_default=False)

        # Deleting field 'Testimonial.quote_name'
        db.delete_column('life_testimonial', 'quote_name')

        # Adding field 'Faq.answer'
        db.add_column('life_faq', 'answer', self.gf('django.db.models.fields.TextField')(default='asdf'), keep_default=False)

        # Adding field 'Faq.question'
        db.add_column('life_faq', 'question', self.gf('django.db.models.fields.CharField')(default='asdf', max_length=200), keep_default=False)

        # Adding field 'Faq.title'
        db.add_column('life_faq', 'title', self.gf('django.db.models.fields.CharField')(default='asdf', max_length=200), keep_default=False)

        # Deleting field 'Faq.name'
        db.delete_column('life_faq', 'name')


    models = {
        'life.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'life.branch': {
            'Meta': {'object_name': 'Branch'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Address']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'contact_person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.StaffMember']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.faq': {
            'Meta': {'object_name': 'Faq'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'life.faqanswertranslation': {
            'Meta': {'object_name': 'FaqAnswerTranslation'},
            'answer_translation': ('django.db.models.fields.TextField', [], {}),
            'faq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Faq']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"})
        },
        'life.faqtranslation': {
            'Meta': {'object_name': 'FaqTranslation'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'faq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Faq']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'life.language': {
            'Meta': {'object_name': 'Language'},
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'life.property': {
            'Meta': {'object_name': 'Property'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Address']"}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Branch']"}),
            'parking': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'property_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'tenure_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'life.propertydescription': {
            'Meta': {'object_name': 'PropertyDescription'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Property']"}),
            'short_desc': ('django.db.models.fields.TextField', [], {})
        },
        'life.propertythumbnail': {
            'Meta': {'object_name': 'PropertyThumbnail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Property']"})
        },
        'life.staffmember': {
            'Meta': {'object_name': 'StaffMember'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['life.Language']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'life.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quote_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        'life.testimonialtranslation': {
            'Meta': {'object_name': 'TestimonialTranslation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'langauge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'testimonial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Testimonial']"})
        },
        'life.textelement': {
            'Meta': {'object_name': 'TextElement'},
            'element_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'life.textelementtranslation': {
            'Meta': {'object_name': 'TextElementTranslation'},
            'element_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.TextElement']"}),
            'element_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"})
        }
    }

    complete_apps = ['life']
