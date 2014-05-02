# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Designer'
        db.delete_table(u'products_designer')

        # Deleting model 'Boutique'
        db.delete_table(u'products_boutique')


        # Changing field 'Product.boutique'
        db.alter_column(u'products_product', 'boutique_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['boutiques.Boutique']))

        # Changing field 'Product.designer'
        db.alter_column(u'products_product', 'designer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['designers.Designer']))

    def backwards(self, orm):
        # Adding model 'Designer'
        db.create_table(u'products_designer', (
            ('specialites', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('label_name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
        ))
        db.send_create_signal(u'products', ['Designer'])

        # Adding model 'Boutique'
        db.create_table(u'products_boutique', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('boutique_website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Designer'])),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal(u'products', ['Boutique'])


        # Changing field 'Product.boutique'
        db.alter_column(u'products_product', 'boutique_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Boutique']))

        # Changing field 'Product.designer'
        db.alter_column(u'products_product', 'designer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Designer']))

    models = {
        u'boutiques.boutique': {
            'Meta': {'object_name': 'Boutique'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'boutique_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['designers.Designer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'designers.designer': {
            'Meta': {'object_name': 'Designer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'label_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'specialites': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'boutique': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boutiques.Boutique']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.ProductCategory']"}),
            'color_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['designers.Designer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'novelty': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'old_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'product_tags': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'size_types': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_by': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        u'products.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['products']