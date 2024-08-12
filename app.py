import streamlit as st 



st.set_page_config(layout='centered')

st.markdown("""
    <style>
    .custom-title {
        font-size: 70px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)











st.markdown('<p class="custom-title"> تبغى وظيفة؟/p>', unsafe_allow_html=True)


Welcome_text = '''
<div style="text-align: Center"> 
توك متخرج؟ شغال على نفسك وجالس تطور مهاراتك بس رزقك ما جاك؟ لا تشيل هم الرزق على رب العباد بلا شك بس العبد لازم يبحث ويسعى بالمكان الصح كمان، 

ان شاء الله بهذه المقالة بنستعرض تمركز الوظائف المتاحة حاليا قطاع خاص؟ قطاع حكومي؟ طيب بأي مدينة؟ الرياض؟ 
</div>
'''
st.html(Welcome_text)





second = '''
<div style="text-align: right"> 
أول ما يخطر بالبال لما نتكلم عن الوظائف هي العاصمة الحبيبة بحكم أنها المقر الرئيسي لعدد كبير من الشركات فمن الطبيعي أن التمركز يكون هنا. 
وبيكون معاك حق، الرياض مهيمنة من ناحية عدد الوظائف
</div>
'''

st.html(second)

#First
st.image('jobs_per_gender.png')




third = '''
<div style="text-align: right"> 

طيب عرفنا أن الرياض مهيمنة وفيه مناطق فيها وظائف كمان زي منطقة مكة والمنطقة الشرقية، بس بالنسبة للتنافس بين الجنسين؟ هل فيه تنافس؟ هل فيه وظائف تتطلب جنس معين دون الآخر؟ 

</div>
'''

st.html(third)

st.image('jobs_per_gender.png')



forth = '''
<div style="text-align: right"> 

اوكي مب سيئ فيه كثير من الوظائف تتطلب الجنسين بدون تمييز والتوزيع للوظائف الي تتطلب جنس دون الاخر قريب من بعض فما فيه اشكال! 


طيب بالنسبة للرواتب؟؟ $$$$ هل ارفع توقعاتي لأول مرتب كشخص خريج حديث؟ كم المتوقع بالنسبة لشخص توه متخرج؟ 
نشوف الصور تقول ان المتوقع ما بين ال 5 الاف إلى حول ال 7 الاف. 

</div>
'''

st.html(forth)

# Third
st.image('expected_salary.png')





sixth = '''
<div style="text-align: right"> 

بالنهاية أتمنى أنك استفدت وزي ما اتفقنا

الرياض هي اعلى المناطق من ناحية الوظائف 

كثير من الوظائف لا تبالي بالجنس 

الراتب المتوقع لحديث التخرج بدون خبرة من 5 إلى 7 الاف. 

وأسال الله ان يرزقك خير ما يرضى. 
</div>

'''

st.html(sixth)