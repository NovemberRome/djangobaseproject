# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arche', '0001_initial'),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='has_contributor',
            field=models.ManyToManyField(blank=True, help_text='Agent (person, group, organisation) (B) who was actively involved in         creating/curating/editing a Resource, a Collection or in a Project (A).', related_name='contributes_to_project', to='entities.Person', verbose_name='acdh:hasContributor'),
        ),
        migrations.AddField(
            model_name='project',
            name='has_funder',
            field=models.ManyToManyField(blank=True, help_text='Organisation (B) which provided funding for the project (A).', related_name='is_funding', to='entities.Institution', verbose_name='acdh:hasFunder'),
        ),
        migrations.AddField(
            model_name='project',
            name='has_principal',
            field=models.ManyToManyField(blank=True, help_text='Person officially designated as head of project team or subproject         team instrumental in the work necessary to development of the resource.', related_name='is_principal', to='entities.Person', verbose_name='acdh:hasPrincipalInvestigator'),
        ),
        migrations.AddField(
            model_name='project',
            name='related_collection',
            field=models.ManyToManyField(blank=True, help_text='Indication of a project (B) associated with this resource or collection (A).', related_name='has_related_project', to='arche.Collection', verbose_name='acdh:hasRelatedCollection'),
        ),
        migrations.AddField(
            model_name='collection',
            name='has_contributor',
            field=models.ManyToManyField(blank=True, help_text='Agent (person, group, organisation) (B) who was actively involved in         creating/curating/editing a Resource, a Collection or in a Project (A).', related_name='contributes_to_collection', to='entities.Person', verbose_name='acdh:hasContributor'),
        ),
        migrations.AddField(
            model_name='collection',
            name='part_of',
            field=models.ForeignKey(blank=True, help_text='Indicates A is a part of aggregate B,         e. g. elements of a series, items of a collection.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='has_part', to='arche.Collection', verbose_name='acdh:isPartOf'),
        ),
    ]