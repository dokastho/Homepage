import PropTypes from 'prop-types';
import React from 'react'
import { render } from 'react-dom';
import Thumbnail from './thumbnail'
import CreatePage from './create';

class Homepage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      logname: "",
      pages: props.pages
    };
    // this.addThumbnail = this.addThumbnail.bind(this)
  }

  componentDidMount() {
    // fetch all the pages, set state
    fetch("/api/v1/page/fetchall/", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({ logname: data.logname, pages: data.pages });
      })
      .catch((error) => console.log(error));
  }

  addThumbnail(page) {
    const { pages } = this.state;
    pages.push(page)
    this.setState({ pages })
  }

  render() {
    const { logname, pages } = this.state;
    var loggedIn = true;
    if (logname === null) {
      loggedIn = false;
    }
    return (
      <div className="wrapper">
        {
          pages.map((page) => (
            <Thumbnail 
              title={page.title}
              description={page.description}
              pageSize={page.pageSize}
            />
          ))
        }
        {
          loggedIn ? (<CreatePage addFunc={this.addThumbnail.bind(this)}/>) : (null)
        }
      </div>
    );
  }
}

Homepage.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
  pages: PropTypes.instanceOf(Array)
};

Homepage.defaultProps = {
  // default prop values go here if not required
  pages: []
};

render(
  <div>
    <Homepage />
  </div>,
  document.getElementById('reactEntry'),
);