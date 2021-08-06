"""
Model exported as python.
Name : esondazione
Group : 
With QGIS : 32001
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterRasterLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Esondazione(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('edifici', 'edifici', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('fiumi', 'fiumi', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterLayer('dtm', 'dtm', defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Estrazione', 'estrazione', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Campionato_valore', 'campionato_valore', type=QgsProcessing.TypeVectorPoint, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        results = {}
        outputs = {}

        # Buffer
        alg_params = {
            'DISSOLVE': True,
            'DISTANCE': 150,
            'END_CAP_STYLE': 0,  # Arrotondato
            'INPUT': parameters['fiumi'],
            'JOIN_STYLE': 0,  # Arrotondato
            'MITER_LIMIT': 2,
            'SEGMENTS': 5,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Buffer'] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Centroidi
        alg_params = {
            'ALL_PARTS': False,
            'INPUT': parameters['edifici'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Centroidi'] = processing.run('native:centroids', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Estrai per posizione
        alg_params = {
            'INPUT': outputs['Centroidi']['OUTPUT'],
            'INTERSECT': outputs['Buffer']['OUTPUT'],
            'PREDICATE': [0],  # interseca
            'OUTPUT': parameters['Estrazione']
        }
        outputs['EstraiPerPosizione'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Estrazione'] = outputs['EstraiPerPosizione']['OUTPUT']

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # campiona_raster  AGGIUNTO
        alg_params = {
            'COLUMN_PREFIX': 'dtm_',
            'INPUT': outputs['EstraiPerPosizione']['OUTPUT'],
            'RASTERCOPY': parameters['dtm'],
            'OUTPUT': parameters['Campionato_valore']
        }
        outputs['Campiona_raster'] = processing.run('native:rastersampling', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Campionato_valore'] = outputs['Campiona_raster']['OUTPUT']
        return results

    def name(self):
        return 'esondazione'

    def displayName(self):
        return 'esondazione'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Esondazione()
