# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'StaffMember'
        db.create_table('life_staffmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('life', ['StaffMember'])

        # Adding model 'Language'
        db.create_table('life_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lang_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('lang', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('flag', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('life', ['Language'])

        # Adding model 'Faq'
        db.create_table('life_faq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('life', ['Faq'])

        # Adding model 'Testimonial'
        db.create_table('life_testimonial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('life', ['Testimonial'])

        # Adding model 'TextElement'
        db.create_table('life_textelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('element_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('life', ['TextElement'])

        # Adding model 'TextElementTranslation'
        db.create_table('life_textelementtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('element_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.TextElement'])),
            ('element_text', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
        ))
        db.send_create_signal('life', ['TextElementTranslation'])


    def backwards(self, orm):
        
        # Deleting model 'StaffMember'
        db.delete_table('life_staffmember')

        # Deleting model 'Language'
        db.delete_table('life_language')

        # Deleting model 'Faq'
        db.delete_table('life_faq')

        # Deleting model 'Testimonial'
        db.delete_table('life_testimonial')

        # Deleting model 'TextElement'
        db.delete_table('life_textelement')

        # Deleting model 'TextElementTranslation'
        db.delete_table('life_textelementtranslation')


    models = {
        'life.faq': {
            'Meta': {'object_name': 'Faq'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'life.language': {
            'Meta': {'object_name': 'Language'},
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'life.staffmember': {
            'Meta': {'object_name': 'StaffMember'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'life.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quote': ('django.db.models.fields.TextField', [], {})
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
