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
      blownUpThumbnail: 0,
      pages: []
    };
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

  // Hook passed to CreatePage component.
  // Appends a thumbnail to the pages array after it was created
  // The request to create a new thumbnail is handled in the CreatePage component.
  addThumbnail(page) {
    const { pages } = this.state;
    pages.push(page)
    this.setState({ pages })
  }
  
  // Hook passed to Thumbnail component.
  // Sets the "blownUpThumbnail" state variable to the thumbnail that was clicked
  // invokes render() due to setState() invocation, which then renders the thumbnail
  // as a center stage Page component
  thumbnailBlowUp(pageId) {
    this.setState({ blownUpThumbnail: pageId });
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

render(
  <div>
    <Homepage />
  </div>,
  document.getElementById('reactEntry'),
);