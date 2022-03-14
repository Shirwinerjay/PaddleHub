import paddle
import math


class ONNXModel(paddle.nn.Layer):
    def __init__(self):
        super(ONNXModel, self).__init__()
        self.conv0 = paddle.nn.Conv2D(in_channels=3, out_channels=3, kernel_size=[1, 1], groups=3)
        self.pool0 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.pool1 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.conv1 = paddle.nn.Conv2D(in_channels=4, out_channels=32, kernel_size=[3, 3], padding=1)
        self.pool2 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.leakyrelu0 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.pool3 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.batchnorm0 = paddle.nn.BatchNorm(
            num_channels=32, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv2 = paddle.nn.Conv2D(in_channels=32, out_channels=32, kernel_size=[3, 3], padding=1)
        self.leakyrelu1 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm1 = paddle.nn.BatchNorm(
            num_channels=32, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.pool4 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.conv3 = paddle.nn.Conv2D(in_channels=32, out_channels=64, kernel_size=[3, 3], padding=1)
        self.leakyrelu2 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm2 = paddle.nn.BatchNorm(
            num_channels=64, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv4 = paddle.nn.Conv2D(in_channels=64, out_channels=64, kernel_size=[3, 3], padding=1)
        self.leakyrelu3 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm3 = paddle.nn.BatchNorm(
            num_channels=64, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.pool5 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.conv5 = paddle.nn.Conv2D(in_channels=64, out_channels=128, kernel_size=[3, 3], padding=1)
        self.leakyrelu4 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm4 = paddle.nn.BatchNorm(
            num_channels=128, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv6 = paddle.nn.Conv2D(in_channels=128, out_channels=128, kernel_size=[3, 3], padding=1)
        self.leakyrelu5 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm5 = paddle.nn.BatchNorm(
            num_channels=128, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.pool6 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.conv7 = paddle.nn.Conv2D(in_channels=128, out_channels=256, kernel_size=[3, 3], padding=1)
        self.leakyrelu6 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm6 = paddle.nn.BatchNorm(
            num_channels=256, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv8 = paddle.nn.Conv2D(in_channels=256, out_channels=256, kernel_size=[3, 3], padding=1)
        self.leakyrelu7 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm7 = paddle.nn.BatchNorm(
            num_channels=256, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.pool7 = paddle.nn.MaxPool2D(kernel_size=[2, 2], stride=2)
        self.conv9 = paddle.nn.Conv2D(in_channels=256, out_channels=512, kernel_size=[3, 3], padding=1)
        self.leakyrelu8 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm8 = paddle.nn.BatchNorm(
            num_channels=512, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv10 = paddle.nn.Conv2D(in_channels=512, out_channels=512, kernel_size=[3, 3], padding=1)
        self.leakyrelu9 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm9 = paddle.nn.BatchNorm(
            num_channels=512, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv11 = paddle.nn.Conv2D(in_channels=512, out_channels=256, kernel_size=[3, 3], padding=1)
        self.conv12 = paddle.nn.Conv2D(in_channels=512, out_channels=256, kernel_size=[3, 3], padding=1)
        self.leakyrelu10 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm10 = paddle.nn.BatchNorm(
            num_channels=256, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv13 = paddle.nn.Conv2D(in_channels=256, out_channels=256, kernel_size=[3, 3], padding=1)
        self.leakyrelu11 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm11 = paddle.nn.BatchNorm(
            num_channels=256, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv14 = paddle.nn.Conv2D(in_channels=256, out_channels=128, kernel_size=[3, 3], padding=1)
        self.conv15 = paddle.nn.Conv2D(in_channels=256, out_channels=128, kernel_size=[3, 3], padding=1)
        self.leakyrelu12 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm12 = paddle.nn.BatchNorm(
            num_channels=128, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv16 = paddle.nn.Conv2D(in_channels=128, out_channels=128, kernel_size=[3, 3], padding=1)
        self.leakyrelu13 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm13 = paddle.nn.BatchNorm(
            num_channels=128, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv17 = paddle.nn.Conv2D(in_channels=128, out_channels=64, kernel_size=[3, 3], padding=1)
        self.conv18 = paddle.nn.Conv2D(in_channels=128, out_channels=64, kernel_size=[3, 3], padding=1)
        self.leakyrelu14 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm14 = paddle.nn.BatchNorm(
            num_channels=64, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv19 = paddle.nn.Conv2D(in_channels=64, out_channels=64, kernel_size=[3, 3], padding=1)
        self.leakyrelu15 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm15 = paddle.nn.BatchNorm(
            num_channels=64, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv20 = paddle.nn.Conv2D(in_channels=64, out_channels=32, kernel_size=[3, 3], padding=1)
        self.conv21 = paddle.nn.Conv2D(in_channels=64, out_channels=32, kernel_size=[3, 3], padding=1)
        self.leakyrelu16 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.batchnorm16 = paddle.nn.BatchNorm(
            num_channels=32, momentum=0.8999999761581421, epsilon=9.999999747378752e-06, is_test=True)
        self.conv22 = paddle.nn.Conv2D(in_channels=32, out_channels=32, kernel_size=[3, 3], padding=1)
        self.leakyrelu17 = paddle.nn.LeakyReLU(negative_slope=0.20000000298023224)
        self.conv23 = paddle.nn.Conv2D(in_channels=32, out_channels=3, kernel_size=[1, 1])

    def forward(self, x2paddle_input):
        x2paddle_137 = paddle.full(dtype='float32', shape=[1], fill_value=1.0)
        x2paddle_145 = paddle.full(dtype='float32', shape=[1], fill_value=0.29899999499320984)
        x2paddle_147 = paddle.full(dtype='float32', shape=[1], fill_value=0.5870000123977661)
        x2paddle_150 = paddle.full(dtype='float32', shape=[1], fill_value=0.11400000005960464)
        x2paddle_153 = paddle.full(dtype='float32', shape=[1], fill_value=2.0)
        x2paddle_155 = paddle.full(dtype='float32', shape=[1], fill_value=1.0)
        x2paddle_256 = paddle.full(dtype='float32', shape=[1], fill_value=1.0)
        x2paddle_134 = self.conv0(x2paddle_input)
        x2paddle_135, = paddle.split(x=x2paddle_134, num_or_sections=[1])
        x2paddle_257 = paddle.multiply(x=x2paddle_134, y=x2paddle_256)
        x2paddle_136 = paddle.squeeze(x=x2paddle_135, axis=[0])
        x2paddle_138 = paddle.add(x=x2paddle_136, y=x2paddle_137)
        x2paddle_139_p0, x2paddle_139_p1, x2paddle_139_p2 = paddle.split(x=x2paddle_138, num_or_sections=[1, 1, 1])
        x2paddle_142 = paddle.squeeze(x=x2paddle_139_p0, axis=[0])
        x2paddle_143 = paddle.squeeze(x=x2paddle_139_p1, axis=[0])
        x2paddle_144 = paddle.squeeze(x=x2paddle_139_p2, axis=[0])
        x2paddle_146 = paddle.multiply(x=x2paddle_142, y=x2paddle_145)
        x2paddle_148 = paddle.multiply(x=x2paddle_143, y=x2paddle_147)
        x2paddle_151 = paddle.multiply(x=x2paddle_144, y=x2paddle_150)
        x2paddle_149 = paddle.add(x=x2paddle_146, y=x2paddle_148)
        x2paddle_152 = paddle.add(x=x2paddle_149, y=x2paddle_151)
        x2paddle_154 = paddle.divide(x=x2paddle_152, y=x2paddle_153)
        x2paddle_156 = paddle.subtract(x=x2paddle_155, y=x2paddle_154)
        x2paddle_157 = paddle.unsqueeze(x=x2paddle_156, axis=[0])
        x2paddle_158 = paddle.unsqueeze(x=x2paddle_157, axis=[0])
        x2paddle_159 = self.pool0(x2paddle_158)
        x2paddle_163 = paddle.concat(x=[x2paddle_134, x2paddle_158], axis=1)
        x2paddle_160 = self.pool1(x2paddle_159)
        x2paddle_164 = self.conv1(x2paddle_163)
        x2paddle_161 = self.pool2(x2paddle_160)
        x2paddle_165 = self.leakyrelu0(x2paddle_164)
        x2paddle_162 = self.pool3(x2paddle_161)
        x2paddle_166 = self.batchnorm0(x2paddle_165)
        x2paddle_167 = self.conv2(x2paddle_166)
        x2paddle_168 = self.leakyrelu1(x2paddle_167)
        x2paddle_169 = self.batchnorm1(x2paddle_168)
        x2paddle_170 = self.pool4(x2paddle_169)
        x2paddle_246 = paddle.multiply(x=x2paddle_169, y=x2paddle_158)
        x2paddle_171 = self.conv3(x2paddle_170)
        x2paddle_172 = self.leakyrelu2(x2paddle_171)
        x2paddle_173 = self.batchnorm2(x2paddle_172)
        x2paddle_174 = self.conv4(x2paddle_173)
        x2paddle_175 = self.leakyrelu3(x2paddle_174)
        x2paddle_176 = self.batchnorm3(x2paddle_175)
        x2paddle_177 = self.pool5(x2paddle_176)
        x2paddle_232 = paddle.multiply(x=x2paddle_176, y=x2paddle_159)
        x2paddle_178 = self.conv5(x2paddle_177)
        x2paddle_179 = self.leakyrelu4(x2paddle_178)
        x2paddle_180 = self.batchnorm4(x2paddle_179)
        x2paddle_181 = self.conv6(x2paddle_180)
        x2paddle_182 = self.leakyrelu5(x2paddle_181)
        x2paddle_183 = self.batchnorm5(x2paddle_182)
        x2paddle_184 = self.pool6(x2paddle_183)
        x2paddle_218 = paddle.multiply(x=x2paddle_183, y=x2paddle_160)
        x2paddle_185 = self.conv7(x2paddle_184)
        x2paddle_186 = self.leakyrelu6(x2paddle_185)
        x2paddle_187 = self.batchnorm6(x2paddle_186)
        x2paddle_188 = self.conv8(x2paddle_187)
        x2paddle_189 = self.leakyrelu7(x2paddle_188)
        x2paddle_190 = self.batchnorm7(x2paddle_189)
        x2paddle_191 = self.pool7(x2paddle_190)
        x2paddle_204 = paddle.multiply(x=x2paddle_190, y=x2paddle_161)
        x2paddle_192 = self.conv9(x2paddle_191)
        x2paddle_193 = self.leakyrelu8(x2paddle_192)
        x2paddle_194 = self.batchnorm8(x2paddle_193)
        x2paddle_195 = paddle.multiply(x=x2paddle_194, y=x2paddle_162)
        x2paddle_196 = self.conv10(x2paddle_195)
        x2paddle_197 = self.leakyrelu9(x2paddle_196)
        x2paddle_198 = self.batchnorm9(x2paddle_197)
        x2paddle_203 = paddle.nn.functional.interpolate(x=x2paddle_198, scale_factor=[2.0, 2.0], mode='bilinear')
        x2paddle_205 = self.conv11(x2paddle_203)
        x2paddle_206 = paddle.concat(x=[x2paddle_205, x2paddle_204], axis=1)
        x2paddle_207 = self.conv12(x2paddle_206)
        x2paddle_208 = self.leakyrelu10(x2paddle_207)
        x2paddle_209 = self.batchnorm10(x2paddle_208)
        x2paddle_210 = self.conv13(x2paddle_209)
        x2paddle_211 = self.leakyrelu11(x2paddle_210)
        x2paddle_212 = self.batchnorm11(x2paddle_211)
        x2paddle_217 = paddle.nn.functional.interpolate(x=x2paddle_212, scale_factor=[2.0, 2.0], mode='bilinear')
        x2paddle_219 = self.conv14(x2paddle_217)
        x2paddle_220 = paddle.concat(x=[x2paddle_219, x2paddle_218], axis=1)
        x2paddle_221 = self.conv15(x2paddle_220)
        x2paddle_222 = self.leakyrelu12(x2paddle_221)
        x2paddle_223 = self.batchnorm12(x2paddle_222)
        x2paddle_224 = self.conv16(x2paddle_223)
        x2paddle_225 = self.leakyrelu13(x2paddle_224)
        x2paddle_226 = self.batchnorm13(x2paddle_225)
        x2paddle_231 = paddle.nn.functional.interpolate(x=x2paddle_226, scale_factor=[2.0, 2.0], mode='bilinear')
        x2paddle_233 = self.conv17(x2paddle_231)
        x2paddle_234 = paddle.concat(x=[x2paddle_233, x2paddle_232], axis=1)
        x2paddle_235 = self.conv18(x2paddle_234)
        x2paddle_236 = self.leakyrelu14(x2paddle_235)
        x2paddle_237 = self.batchnorm14(x2paddle_236)
        x2paddle_238 = self.conv19(x2paddle_237)
        x2paddle_239 = self.leakyrelu15(x2paddle_238)
        x2paddle_240 = self.batchnorm15(x2paddle_239)
        x2paddle_245 = paddle.nn.functional.interpolate(x=x2paddle_240, scale_factor=[2.0, 2.0], mode='bilinear')
        x2paddle_247 = self.conv20(x2paddle_245)
        x2paddle_248 = paddle.concat(x=[x2paddle_247, x2paddle_246], axis=1)
        x2paddle_249 = self.conv21(x2paddle_248)
        x2paddle_250 = self.leakyrelu16(x2paddle_249)
        x2paddle_251 = self.batchnorm16(x2paddle_250)
        x2paddle_252 = self.conv22(x2paddle_251)
        x2paddle_253 = self.leakyrelu17(x2paddle_252)
        x2paddle_254 = self.conv23(x2paddle_253)
        x2paddle_255 = paddle.multiply(x=x2paddle_254, y=x2paddle_158)
        x2paddle_output = paddle.add(x=x2paddle_255, y=x2paddle_257)
        return x2paddle_output, x2paddle_255
