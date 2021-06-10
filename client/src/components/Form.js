import {useForm} from 'react-hook-form'

const Form = (setPosition) => {

    const {register, handleSubmit, formState: { errors} } = useForm() //Add handlesubmit

    return (
        <> 
        <form onSubmit={handleSubmit((data) => {setPosition(data)})}>
          <input type="text" name='keyword' placeholder='Keywords' {...register('x', {required: false})}/> <br />

          <input type="text" name='state' placeholder='State' {...register('y', {required: true})}/> <br />
          {errors.state && <p>State is required</p>}
        
          <input type="text" name='city' placeholder='City'{...register('city', {required: true})}/> <br />
          {errors.date && <p>City is required</p>}

          <input type="text" name='postal-code' placeholder='Postal Code' {...register('postal-code', {required: true})}/> <br />
          {errors.date && <p>Postal code is required</p>}

          <input type="number" name='radius' placeholder='Radius' {...register('radius', {required: true})}/> <br />
          {errors.date && <p>Radius is required</p>}

          <input className='button' type="submit" name='submit' value='Feed me'/>
          
        </form>
    
        </>
    )
}

export default Form
