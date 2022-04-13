import pixellib
from pixellib.tune_bg import alter_bg
from pixellib.instance import custom_segmentation


alter = alter_bg()
alter.load_pascalvoc_model('modelos/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5')
#alter.color_bg('ninos.jpg',colors=(150,120,75),output_image_name='ninos2.jpg',detect='person')
#alter.color_bg('botellaP.jpg',colors=(150,120,75),output_image_name='botellaP2.jpg',detect='bottle')
alter.color_bg('carro.jpg',colors=(255,255,255),output_image_name='carro2.jpg',detect='car')
#alter.change_bg_img('chama.jpg','blanco.png', output_image_name='chama3.jpg',detect='person')









'''
segmentationModel = custom_segmentation()
segmentationModel.inferConfig(num_classes=1, class_names=['dog'])
segmentationModel.load_model('yolo.h5')
segmentationModel.segmentImage('perroSuerte.jpeg', output_image_name='salidaPerro.jpg')
'''