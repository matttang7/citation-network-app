import React from 'react';
import axios from 'axios';

export default class AuthorSearch extends React.Component {
  state = {
    name: '',
    list: []
  }

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const user = {
      name: this.state.name
    };

    axios.get(`http://127.0.0.1:5000/get/${this.state.name}`)
      .then(res => {
        console.log(res.data);
        this.setState({ list: res.data })
      })
  }

  render() {
    return (
      <div>
        Search for author's most frequently cited papers:
        <form onSubmit={this.handleSubmit}>
          <label>
            Author Name:
            <input type="text" name="name to search" onChange={this.handleChange} />
          </label>
          <button type="submit">Search</button>
        </form>

        <ul>
          Paper Id, Number of times Referenced
          {this.state.list.map(function(item) {
            return <li key={item}>{item[0]}, {item[1]}</li>;
          })}
        </ul>
      </div>
      
    )
  }
}