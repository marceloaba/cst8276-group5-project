import {useForm} from 'react-hook-form'

/**
 * Form component to pass the data to get results from the API.
 * react-hook-form library is used to automatically handle the
 * submission and the errors. 
 * @author Apo Ilgun
 */
const Form = ({getData}) => {

    const {register, handleSubmit, formState: { errors} } = useForm() 

    return (
        <> 
        <form className='form' onSubmit={handleSubmit((data) => {getData(data)})}>
          <input type="text" name='name' placeholder='Keywords' {...register('name', {required: true})}/> <br /> 

          <input type="text" name='postal-code' placeholder='Postal Code' {...register('zipCode', {required: true})}/> <br />
          {errors.date && <p>Postal code is required</p>}

          <input type="number" name='radius' placeholder='Radius' {...register('radius', {required: false})}/> <br />
          {errors.date && <p>Radius is required</p>}

          <input className='button' type="submit" name='submit' value='Feed me'/>

        </form>
        </>
    )
}

export default Form
